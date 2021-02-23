import datetime
from psycopg2.extras import Json

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
