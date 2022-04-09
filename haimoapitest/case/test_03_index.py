import json
import requests
import pytest
import random
import os, sys
sys.path.append(os.getcwd())
from utils.config import ServerInFo
from utils.mysqltools import MysqlTools



def test_01_home_page(user_login):
    """
    首页登陆接口
    """
    url = ServerInFo().get_url('/haimo/sass/homePage/sassHomePage')
    header = {"token":user_login}
    res = requests.post(url=url,headers=header)
    assert res.status_code == 200
    assert res.json()['code'] == 1


def test_02_entry_daily(user_login):
    """
    录入报告今日
    """
    url = ServerInFo().get_url('/haimo/sass/homePage/reportEntryDaily')
    header = {"token":user_login}
    res = requests.post(url=url,headers=header)
    assert res.status_code == 200
    assert res.json()['code'] == 1


def test_03_entry_monthly(user_login):
    """
    录入报告月度
    """
    url = ServerInFo().get_url('/haimo/sass/homePage/reportEntryMonthly')
    header = {"token":user_login}
    data = {"date":1630568901000}
    res = requests.post(url=url,headers=header)
    assert res.status_code == 200
    assert res.json()['code'] == 1



def test_04_entry_everyyear(user_login):
    """
    录入报告年度
    """
    url = ServerInFo().get_url('/haimo/sass/homePage/reportEntryEveryYear')
    header = {"token":user_login}
    data = {"date":1630568901000}
    res = requests.post(url=url,headers=header)
    assert res.status_code == 200
    assert res.json()['code'] == 1



def test_05_entry_everyyear(user_login):
    """
    录入档案月度
    """
    url = ServerInFo().get_url('/haimo/sass/homePage/recordMonthly')
    header = {"token":user_login}
    data = {"date":1630568901000}
    res = requests.post(url=url,headers=header)
    assert res.status_code == 200
    assert res.json()['code'] == 1



def test_06_entry_everyyear(user_login):
    """
    录入档案年度
    """
    url = ServerInFo().get_url('/haimo/sass/homePage/recordEveryYear')
    header = {"token":user_login}
    data = {"date":1630568901000}
    res = requests.post(url=url,headers=header)
    assert res.status_code == 200
    assert res.json()['code'] == 1


def test_07_entry_inputfileseveryday(user_login):
    """
    输入记录每日
    """
    url = ServerInFo().get_url('/haimo/sass/homePage/inputFilesEveryDay')
    header = {"token":user_login}
    data = {"date":1630568901000}
    res = requests.post(url=url,headers=header)
    assert res.status_code == 200
    assert res.json()['code'] == 1



