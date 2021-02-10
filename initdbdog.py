import yaml

def get_dog_instance_info(dogpath):
    """
    获取配置文件
    """
    with open(dogpath) as dogp:
        dogy=yaml.safe_load(dogp)
    dog_db_host=dogy['db']['host']
    dog_db_port=dogy['db']['port']
    dog_db_db=dogy['db']['db']
    dog_db_user=dogy['db']['user']
    dog_db_pass=dogy['db']['pass']
    return [dog_db_host,dog_db_port,dog_db_db,dog_db_user,dog_db_pass]