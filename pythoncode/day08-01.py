# 1.导入库
import requests
from mysqltools import MysqlTools
# 2.构造请求（用变量定义地址 传参 get/post方法获取地址和参数）
u = "http://ljtest.liuyun.tech:28080/haimo/sass/systemUser/release/getLogin"
d = {"userName":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
res = requests.post(url=u,json = d)
print(res.text)  #断言上做打印返回值操作判断断言出问题
# 3.断言结果
assert res.status_code == 200
assert res.json()["code"] == 1
#4. 关联
token = res.json()["data"][0]["token"]
# token = res.json()["data"]["token"]
# print(token[0]["token"])

username = "liuyun16"
u1 = "http://ljtest.liuyun.tech:28080/haimo/sass/systemUser/addSystemUser"
d1 = {"loginAccount":username,"loginPassword":"e9bc0e13a8a16cbb07b175d92a113126","realName":"","categoryId":[]}
h1 = {"token": token}

res = requests.post(url=u1, json=d1, headers=h1)
assert res.status_code ==200
assert res.json()["code"] == 1

# 查询的条件》账号存在数据库 》查询结果长度不等于0 》注册接口是把数据写入到数据库中 》新增系统用户功能是正常的
sql = "select * from tb_system_user where login_account='{}'".format(username)
q_res = MysqlTools().query(sql)
assert len(q_res) != 0
# 发表灵感
print("新增系统用户成功！")

# print(token)
# print("登陆成功！")






u2 = "http://ljtest.liuyun.tech:28080/haimo/sass/systemUser/listSystemUser/1/10"
h2 = {"token": token}
d2 = {"loginAccount":username}
resp = requests.post(url=u2, json=d2, headers=h2)
assert resp.status_code == 200
assert resp.json()["code"] == 1

# 问题：这里需要做数据库查询吗？
# 回答：不需要
print("查询成功")
