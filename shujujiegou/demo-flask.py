# 第一个简单的接口
from flask import Flask
from flask import request   #内置的变量
from tokenGenerator import token_Generator
import pymysql  #导入pymysql
from redistools import set_redis
from redistools import get_redis
from redistools import del_redis
from mysqltools import query   #导入封装的数据库查询方法
from datetime import datetime
from mysqltools import update




# 1.初始化flask插件
app = Flask(__name__)

# print(__name__)

# __name__ :python的内置变量
# __doc__ :函数，方法的说明


#2.使用flask自带的装饰器去定义一个接口，接口以方法形式存在

@app.route("/") #接口的路径是 /
def index():
    return "这是flask"

# 3.
# http://127.0.0.1:5000/getUserList?pageNum=1   # get的传参格式
@app.route("/getUserList",methods = ['get']) # ==@app.route("/getUserList"),get methods=['get'] 可以忽略
def get_user_list():
    # 接口get类型的参数
    page_num = request.args.get('pageNum')

    return page_num



# post接口
@app.route("/login",methods =["post"])
def login():
    username = request.args.get("username")
    password = request.args.get("password")


    # #连接数据库 ， 连上数据库之后会返回数据库的连接对象
    # db = pymysql.connect(host='119.45.233.102', port=3306, user='testgoup', password='1qaz!QAZ', db="flaskdemo")

    # # 获取查询窗口的权限：游标
    # cur = db.cursor()

    # #执行查询语句

    # sql = "select * from tb_user where username = '{}'and password = '{}' and status = 1 ".format("username","password")
    # # 执行sql语句的执行,查询你得账号密码在不在数据库当中
    # cur.execute(sql)
    # result = cur.fetchall()    #把sql语句的查询结果保存到result变量中

    # db.close()    # 关闭数据库
    
    sql = "select * from tb_user where username = '{}'and password = '{}' and status = 1 ".format("username","password")
    result = query(sql)

    if len(result) == 1:     # 这里为什么是等于1呢，因为sql结果返回的是一个二维元组  #查到结果了》where条件有结果 》 说明数据库中的这个账号是真实有效的
        token  = token_Generator()
        if set_redis(token,result[0][0]):
            return {"code":1,"msg":"登陆成功","data":[{"token":"token"}]}    #这里的传给前端的data 为什么要用列表去传呢？？？？？
        else:
            return {"code":0,"msg":"登陆失败，账号密码错误","data":[]}
    else:
        return {"code":0,"msg":"登陆失败，账号密码错误","data":[]}


    # if username == "admin" and password =="123456":     #如果查到了结果就是一个二维元组
    #     data = {"code":1,"msg":"登录成功","data":[]}
    # else:
    #     data = {"code":0,"msg":"登录失败","data":[]}

    # # {"code":1,"msg":"登陆成功"，"data":[]} : 传参的时候称为json，在python中称为字典，所以返回值需要变成标准resetfu接口
    # data = {
    #         "code":1,
    #         "msg":"登陆成功",
    #         "data":[]
    #         }

    # return data

# 注册接口
@app.route("/regist",methods = ["post"])
def regist():
    
    username = request.args.get("username")
    password = request.args.get("password")
    nickname = request.args.get("nickname")

    sql = """select * from tb_user where username='{} and password = {} and nickname = {}'""".format(username, password,nickname)
    result = query(sql)
    # ------------------------------------------------------------- 更新到此处
    if len(result) != 0:
        return {"code":"0","msg":"注册失败，账号已经注册过了","data":[]}
    else:
        insert_user_sql = """insert into tb_user values(null, '{}', '{}', '{}', 1, '{}')""".format(
            username, password, nickname, datetime.now())
        if update(insert_user_sql) is True:
            return {"code":"1","msg":"注册成功","data":[]}
        else:
            return {"code":"0","msg":"注册失败，请联系管理员","data":[]}




    # if username == "admin" and password == "123456":
    #     data = {
    #         "code":0,
    #         "msg":"注册失败，账号已经被注册过了",
    #         "data":[]
    #         }
    # elif 5<= len("username") <=10 and 8<= len("password")<=20:
    #     data = {
    #         "code":111,
    #         "msg":"注册成功",
    #         "data":[]
    #         }


    # 数据库查询，判断表中是否存在相同账号，以账号为唯一标识来校验
    # db = pymysql.connect(host='119.45.233.102', port=3306, user='testgoup', password='1qaz!QAZ', db="flaskdemo")
    # # 获取查询窗口的权限：游标
    # cur = db.cursor()
    # #执行查询语句
    # sql = "select * from tb_user where username = '{}'and password = '{}' ".format("username","password")
    # # 执行sql语句的执行,查询你得账号密码在不在数据库当中
    # cur.execute(sql)
    # result = cur.fetchall()    #把sql语句的查询结果保存到result变量中
    # db.close()    # 关闭数据库
    # sql = "select * from tb_user where username = '{}'and password = '{}' ".format("username","password")
    # result = query(sql)
    # if len(result)!= 0:
    #     data = {"code":0,"msg":"账号已经被注册过了","data":[]}

    # else:
    #     data ={}


    #     data = {
    #         "code":11,
    #         "msg":"注册失败",}

# 分场景去写，先写注册失败的场景 再去写注册成功的场景

    # if "username" == "admin" and "password" == "12345678":
    #         data = {
    #             "code":111,
    #             "msg":"注册失败，",
    #             "data":[]
    #             }
    # elif  len(username) <5 or len(username) >10 or  len(password) > 7 or len(password) >20:
    #     data = {
    #             "code":111,
    #             "msg":"注册失败，",
    #             "data":[]
    #             }


    # else:
    #     data = {
    #         "code":1,
    #         "msg":"注册成功",

    #         "data":[]
    #         }

    # return data


        

    
# 数据库查询



# 4.启动接口



# - host:127.0.0.1:本机ip：自己电脑的 localhost：自己电脑的localhost：只能本机访问，其他的电脑访问不了
# - host：0.0.0.0：监听来自任意的ip地址访问：任何ip地址的电脑都能访问

#port：指定访问端口号，不指定端口号默认为5000

#debug模式:
# debug:Ture，修改代买后，保存一下，自动运行。
# debug：false，关闭debug模式，添加或者修改后，需要手动运行代码

#app.run 的本质是对 from werkzeug.serving import run_simple 的二次封装，options关键字参数给run_simple




#debug mode off/on
# on : 表示接口调试状态是打开的
# off：表示接口调试状态是关闭的
# Running on http://127.0.0.1:5000/  ：  接口请求地址：服务地址+接口路径



# 修改密码接口
@app.route("/UpDateUserPassword",methods = "post")
def UpDateUserPassword():
    token = request.headers.get("token")   # 前端拿到token，后续利用这个token去调用redis方法去取值，取出的userid不为空，则表示有相应的账号，为空则提示请先登录
    new_password = request.json.get("newPassword")
    user_id = get_redis(token)
    if user_id is None:
        return {"code":"0","msg":"请先登录","data":[]}
    update_user_password_sql = """UPDATE tb_user 
                                SET PASSWORD = '{}' 
                                WHERE id ={}""".format(new_password, user_id)
    if update(update_user_password_sql) is True:
        return {"code":1 , "msg":"修改密码成功", "data":[]}
    else:
        return {"code":0 , "msg":"系统异常，请联系管理员", "data":[]}

# 启动接口

app.run(host = "0.0.0.0",port = "5000",debug = True)