import requests as r
from io import BytesIO
import blurhash
from PIL import Image
import hashlib
from dogid import gen_dog_id
import uuid

Headers = {'user-agent': 'Dogcraft misskey instance tools (https://m.dogcraft.top) '}


class DogFile(object):
    """
    文件相关
    """
    name='null'
    dogtype='other'
    bs=None
    size=None

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
            self.name= str(self.urldog.split('/')[-1])[-30:]
            self.ak=str(uuid.uuid4())
            self.tn='thumbnail-{}'.format(uuid.uuid4())
            self.wp='webpublic-{}'.format(uuid.uuid4())
            self.md5=mdog

