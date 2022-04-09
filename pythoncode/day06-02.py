# 1.导入库
import requests
from requests.sessions import RequestsCookieJar
# 2.构造请求（用变量定义地址 传参 get/post方法获取地址和参数）
u = "http://ljtest.liuyun.tech:32333/login"
d = {
"username":"liuyun1",
"password":"a12345678" 
}
res = requests.post(url=u,json = d)
# print(res.text)  #断言上做打印返回值操作判断断言出问题
# 3.断言结果
assert res.status_code == 200
assert res.json()["status"] == 200

token = res.json()["data"]["token"]
print(token)
print("登陆成功！")


u1 = "http://ljtest.liuyun.tech:32333//logout"
h1 = {"Content-Type":"application/json","token":token}
res = requests.get(url=u1,headers = h1)
assert res.status_code == 200
assert res.json()["status"] == 200
print("退出成功！")








