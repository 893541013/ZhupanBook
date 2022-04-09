import requests
from requests import status_codes
# 1.构造请求
u = "http://ljtest.liuyun.tech:32333/get_title_img"

# res 返回值的所有信息(res：响应：（响应头：状态码之类的+返回值）)
res = requests.get(url=u) #使用get方法调用u这个接口，u一定是get类型的
print(res.text) #res.text,获取接口的返回信息
print(res.status_code)  #res.status_code：http状态码
# res.json() == a ==a["status"] > res.json()["status"]

# a = {
#   "data": [
#     {
#       "id": 386, 
#       "imghost": "ximg.jpg", 
#       "rurl": "http://www.baidu.com", 
#       "title": "测试"
#     }, 
#     {
#       "id": 387, 
#       "imghost": "ximg.jpg", 
#       "rurl": "http://www.baidu.com", 
#       "title": "测试"
#     }, 
#     {
#       "id": 388, 
#       "imghost": "ximg.jpg", 
#       "rurl": "http://www.baidu.com", 
#       "title": "测试"
#     }
#   ], 
#   "msg": "操作成功！", 
#   "status": 200
# }
# 2.断言结果
assert res.status_codes == 200 # 200：ok 接口正常的
assert res.json()["status"] ==200 #判断接口返回值是正确的
