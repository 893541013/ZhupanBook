from utils.mysqltools import MysqlTools
import requests
import pytest

#导入日志库
from loguru import logger

logger.info("正在请求https://wwww.baidu.com/") # 输出信息等级：告知步骤
logger.debug("返回值是xxxx") #输出调试信息
logger.error("代码执行异常，检查对应参数") #输出错误信息
logger.critical("自动化测试框架致命的错误，无法继续运行") #输出致命错误信息




# from haimoApiTest.utils.config import get_url  pycharm编辑器
#通过环境变量的方式让项目目录变成主目录
#这样我们就可以在不同文件夹下面导包
import os,sys
sys.path.append(os.getcwd())
# from utils.config import get_url
from utils.config import ServerInFo



def test_01_login_success():
    # 2.构造请求（用变量定义地址 传参 get/post方法获取地址和参数）
    u = ServerInFo.get_url("/haimo/sass/systemUser/release/getLogin")
    d = {"userName":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
    res = requests.post(url=u,json = d)
    assert res.status_code == 200
    assert res.json()["code"] == 1


    #数据库校验
  