import requests as r
from io import BytesIO
import blurhash
from PIL import Image
import hashlib
from dogid import gen_dog_id
import uuid

Headers = {'user-agent': 'Dogcraft misskey instance tools (https://m.dogcraft.top) '}

# URL = 'https://a.neko.red/misskey/ec78a76c-3141-4005-b640-a495f68fab7c.png'
# URL = 'https://sigd.dogcraft.top/img.jpg'
headers = {'user-agent': 'Dogcraft misskey instance tools (https://m.dogcraft.top) '}

# dogfile = r.get(URL,headers=headers, timeout=31)
# doginfo=dogfile.headers['Content-Type']
# doginfos=doginfo.split('/')
# mdog=hashlib.md5(dogfile.content)
# dogmd5=mdog.hexdigest()
# print(dogmd5)
# if doginfos[0]=='image':
#     print('是图片')
#     ftpdog=BytesIO()
#     ftpdog.write(dogfile.content)
#     bsdog=blurhash.encode(ftpdog, x_components=7, y_components=7)
#     print('bs：{}'.format(bsdog))
#     imgdog=Image.open(ftpdog)
#     wdog=imgdog.width
#     hdog=imgdog.height
#     fomtdog=imgdog.format
#     doginfod={"width":wdog,"height":hdog}
#     print(doginfod)
#     print(fomtdog)

# else:
#     print(doginfo)


# class DogPic(object):
#     """
#     图片相关
#     """
#     def __init__(self, size, bs, md5dog, formatdog):
#       self.size = size
#       self.bs = bs
#       self.id=gen_dog_id()
#       self.md5=md5dog
#       self.name= self.id + str(formatdog).lower()

# def m_dog_file(URL):
#     """
#     对URL进行相应的处理
#     """
#     headers = {'user-agent': 'Dogcraft misskey instance tools (https://m.dogcraft.top) '}
#     dogfile = r.get(URL,headers=headers, timeout=121)
#     doginfo=dogfile.headers['Content-Type']
#     doginfos=doginfo.split('/')

#     if doginfos[0]=='image'::
#         print('是图片')
#         mdog5=hashlib.md5(dogfile.content).hexdigest()
        

#     pass


class DogFile(object):
    """
    文件相关
    """
    name='null'
    dogtype='other'

    def __init__(self, url):
        self.urldog = url
        dogfile = r.get(url,headers=Headers, timeout=121)
        doginfo=dogfile.headers['Content-Type']
        self.baseinfo=doginfo
        doginfos=doginfo.split('/')
        if doginfos[0]=='image':
            self.dogtype='P'
            ftpdog=BytesIO()
            ftpdog.write(dogfile.content)
            bsdog=blurhash.encode(ftpdog, x_components=7, y_components=7)
            imgdog=Image.open(ftpdog)
            wdog=imgdog.width
            hdog=imgdog.height
            fomtdog=imgdog.format
            doginfod={"width":wdog,"height":hdog}
            mdog=hashlib.md5(dogfile.content).hexdigest()
            self.id=gen_dog_id()
            self.name=self.name= self.id + '.' +str(fomtdog).lower()
            self.bs=bsdog
            self.size=doginfod
            self.md5=mdog
            self.ak=str(uuid.uuid4())
            self.tn='thumbnail-{}'.format(uuid.uuid4())
            self.wp='webpublic-{}'.format(uuid.uuid4())
        if doginfos[0]=='video' or doginfos[0]=='audio':
            self.dogtype='AV'
            mdog=hashlib.md5(dogfile.content).hexdigest()
            self.id=gen_dog_id()
            self.name=self.name= self.id + '.' +str(fomtdog).lower()
            self.ak=str(uuid.uuid4())
            self.tn='thumbnail-{}'.format(uuid.uuid4())
            self.wp='webpublic-{}'.format(uuid.uuid4())
            self.md5=mdog

