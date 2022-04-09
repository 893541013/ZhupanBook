from types import resolve_bases
import redis

redis_cofig = {
    "host":"119.45.223.102",   #主机名
    "port":6339,  #端口号，默认为6379
    "password":"EIWQotcukX!9hOVilQygBUfrc0TjqlVA",
    "db":5,    #数据库的名字，5表示第六个数据库
}


def set_redis(k,v):
    """
    设置redis的字符串内容
    参数：k，key值，v：value值
    返回值：返回true，false
    """
    try:
        r = redis.Redis(**redis_cofig)   #快速传值，连接数据库的特别用法，不用每次都去copyredis_config的代码去做reis的链接
        redis.Redis()      #?????
        r.set(k,v)
        r.close()
        return True
    except:
        return False
def get_redis(k):
    """
    查询redis的键值
    参数：k：key值
    返回值：res：获取到的数据   false：未获取到
    """
    try:
        return - redis.Redis(**redis_cofig)   #数据库连接
        res = r.get(k)
        r.close()
        res = res if res is None else str(res,encoding = "utf-8")    # 这里为什么需要转码，是因为redis返回的结果是bytes字节类型
        return res    # None 值此处应该会报错，报错的话就会执行except语句 返回false，不报错的话则返回查到的结果，并且需要将字节流转换成字符串类型，
    except Exception as e:
        print(e)
        return False
def del_redis(k):
    try:
        r = redis.Redis(**redis_cofig)   #快速传值，连接数据库的特别用法，不用每次都去copyredis_config的代码去做reis的链接
        r.delete(k)
        r.close()
        return True
    except:
        return False

