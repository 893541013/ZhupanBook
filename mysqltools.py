# pymysql连接并操作数据库

import pymysql

def query(sql):
    """
        方法名:数据查询
        参数:数据库查询sql语句
        返回:（（数据行））
    """
    db = pymysql.connect(host='119.45.233.102', port=3306, user='testgoup', password='1qaz!QAZ', db="flaskdemo")
    cur = db.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    db.close()

    return result


def update(sql):
    """
        方法名:数据查询
        参数:数据库查询sql语句
        返回:（（数据行））
    """
    try:
        db = pymysql.connect(host='119.45.233.102', port=3306, user='testgoup', password='1qaz!QAZ', db="flaskdemo")
        cur = db.cursor()				
        db.commit() # 数据库的commit
        db.close()  # 关闭连接
        return True
    except:
        db.rollback()   # 回滚
        db.close()      # 关闭数据库连接
        return False
