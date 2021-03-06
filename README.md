# mkimg

工作在[DMI](https://m.dogcraft.top/)上的外置式misskey"外链"插件(?)

## 主要解决的问题：

misskey本地用户上传的文件，都会保存在服务器本地或者对象存储，但外部的用户图片，可以保存一个链接，并可以选择代理或者不代理外部文件。如果本地用户的存储空间配额耗尽，将无法上传添加新的媒体文件，如果以外部链接的形式上传发送图片，将不会占据用户的存储空间配额。为了可以使得存储空间配额耗尽的用户可以发图片，特地增加一个API与其配套的专门的html页面。

## 基本原则与思路

为了防止后续版本不兼容，基本原则是不改动misskey程序代码，通过nginx外置页面与api的方式添加“外链”功能。

misskey的所有图片都在`drive_file`这个表里面，可以通过绕过misskey的api直接向这个表里写入数据的方式实现向特定用户的网盘里插入文件(链接)，这个表里的文件的归属实际上是通过用户id来确定的。同时这个API需要对上传图片外链的请求进行鉴权并判断是哪一个用户上传的，所以需要一个认证与访问控制机制。misskey的原生API是通过`i`这个参数进行访问控制的，这个参数是存储在浏览器的`localStorage`，可以用js很方便取出来。在数据库里`public.user`表里面的token列可以对其进行鉴权与并获得用户id。

总的来说并不复杂，需要一个接受两个参数的API，一个是`i`确定用户的身份，另一个是插入的文件的url，在验证用户请求合法之后，再考虑将相关文件的信息插入数据库中。

## 实现方式

既然不改动任何misskey的代码，完全可以用自己最熟悉的语言来安排。这里采用`flask_restful`来安排。页面采用手写的HTML用nginx写了一个`location`来安排进去。同时为了防止一些错误的url被插入数据库，并插入相关`blurhash`等信息，需要先把url下载下来看一看到底是什么种类的文件，如果是图片再获取尺寸等进一步的信息。

具体的代码可以看一系列的`*.py`文件，手写的html可以看pages下面的`index.html`。
