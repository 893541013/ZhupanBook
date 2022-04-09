
import json
import requests
import pytest
import random
import os, sys
sys.path.append(os.getcwd())
from utils.config import ServerInFo
from utils.mysqltools import MysqlTools

# 用户管理模块



def test_01_add_user(user_login):
    """
        添加系统用户
    """
    # token会出现问题，每次运行test方法之前，自动运行登录，然后取出token
    url = ServerInFo.get_url('/haimo/sass/systemUser/addSystemUser')
    header = {"token": user_login}
    name = 'ly' + str(random.randint(10000000, 99999999))
    data = {"loginAccount":name,"loginPassword":"e9bc0e13a8a16cbb07b175d92a113126","categoryId":[]}
    res = requests.post(url=url, header=header, json=data)
    
    assert res.status_code == 200
    assert res.json()['code'] == 1

    # 需要做数据库检查
    sql = "select * from tb_system_user where login_account = '{}' and login_password='c5371f1d7a03cd4b44085d3ada7092df'".format(data["loginAccount"])
    q_res = MysqlTools().query(sql)
    assert len(q_res) != 0



