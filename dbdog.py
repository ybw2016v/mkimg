import datetime
#import psycopg2
from psycopg2.extras import Json


#pgdog = psycopg2.connect(
#        database='misskey', user='misskey', password='dogdogdog', host='192.168.0.112', port=20489)
# sdo=pgdog.cursor()
# # sdo.execute("""select * from drive_file where "id" = '8hxypyuf72';""")
# sdo.execute("""INSERT INTO drive_file VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s );""",lli[0])
# INSERT INTO authors (name) VALUES (%s)
# aasd=datetime.datetime.now()
# lli=[('8hxypyuf79', aasd, '89gargpjc3', 'hello.2heng.xin', '60132b41a0daf71a5feb847ea49b4282', 'cb7063bca3c4f4ce.jpeg', 'image/jpeg', 0, None, Json({'width': 870, 'height': 1884}), False, 'https://s3-hk.2heng.xin/mstdn/media_attachments/files/105/687/095/458/321/702/original/cb7063bca3c4f4ce.jpeg', None, None, 'd7a8d034-aea8-4faf-b0de-01bff076dae0', 'thumbnail-f4147d48-8949-4c7c-8f00-0d48e70b2550', 'webpublic-d785d88e-11c2-43b9-a32a-16836a3d5b00', 'https://s3-hk.2heng.xin/mstdn/media_attachments/files/105/687/095/458/321/702/original/cb7063bca3c4f4ce.jpeg', 'https://s3-hk.2heng.xin/mstdn/media_attachments/files/105/687/095/458/321/702/original/cb7063bca3c4f4ce.jpeg', None, False, True, 'ySLg;JxuRPxuR*t7ay00WBWARjWVRjWB?vj[j?ofWBa{a{_Nfkayofayj[j[8_ayofWVj[ayayI9oKofWBj[ayazt7axofj@ofofj[')]




def write_dog_pic(dogdb,pdog,uidog):
    """
    将图片信息写入数据库
    """
    dogid=pdog.id
    dogtime=datetime.datetime.now()
    doguserid=uidog
    dogmd5=pdog.md5
    dogname=pdog.name
    dogtype=pdog.baseinfo
    dogsize=pdog.size
    dogurl=pdog.urldog
    dogak=pdog.ak
    dogtn=pdog.tn
    dogwp=pdog.wp
    dogbs=pdog.bs
    doglist=(dogid, dogtime, doguserid,None, dogmd5, dogname, dogtype, 0, None, Json(dogsize), False, dogurl, None, None, dogak, dogtn, dogwp, dogurl, dogurl, None, False, True, dogbs)
    print(doglist)
    dogps=dogdb.cursor()
    dogps.execute("""INSERT INTO drive_file VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s );""",doglist)
    dogdb.commit()

def get_dog_id(dogdb,idog):
    """
    由i参数获取用户id
    """
    cdog=dogdb.cursor()
    cdog.execute("""select id from public.user where token = %s;""",(idog,))
    resdog=cdog.fetchone()
    if resdog is not None:
        return resdog[0]
    cdog.execute("""select "userId"  from access_token where token = %s;""",(idog,))
    resdog=cdog.fetchone()
    if resdog is not None:
        return resdog[0]
    return None


# doguid='89fhzj179y'
# tt='OZoL7E89P9PB72Mh'

# tt='TFAhiPVjdtCJwJXDFzOTBZF4eLSvf0PZ'
# uuudidog=DogFile('https://boot-video.xuexi.cn/audio/1005/p/478491f991985def995ae8288af4e38d-c6fe1a0d30104b27b979b11c1d423ed4-1.mp3')
# write_dog_pic(pgdog,uuudidog,doguid)
# print(uuudidog.sdk)
# ssdf=get_dog_id(pgdog,tt)
# print(ssdf)
