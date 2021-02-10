doginfostr = localStorage.getItem('account');

if (doginfostr === null) {
    window.location.href='/';
}
doginfo=JSON.parse(doginfostr);

var Htmldog=`<div class="card-body" id="ddinfo">
<img src="${doginfo.avatarUrl}" class="dogavatar"><span class="dogname">${doginfo.name}</span><span class="dogname">${doginfo.username}@${window.location.host}</span>
<div class="contain cont">
</div>
</div>`;

var Htmldog2= '<div class="alert alert-primary alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>正在上传</strong> 请稍后……</div>';



async function uploaddog() {
    doguploaddata={i:doginfo.token,url:diu.picdog}
    $('#innf').text(Htmldog2);
    uiy = await fetch(ApiUrl, {
        method: 'POST',
        body: JSON.stringify(doguploaddata),
        headers: new Headers({
            'Content-Type': 'application/json'
        })
    });
    if (uiy.status == 200) {
        rt = await uiy.json();
        res_dog = rt.r;
    } else {
        res_dog = '接口不对劲';
    }
    if (res_dog!='success') {
        var Htmldog3= `<div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>错误！</strong> ${res_dog}</div>`;
        $('#innf').text(Htmldog3)

    } else {
        var Htmldog4= `<div class="alert alert-success alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>成功！</strong> ID: ${rt.pid}</div>`;
        $('#innf').text(Htmldog4)
    }
}
