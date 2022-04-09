# user = ["zhangsan","a12345678"]
# username = input("请输入账号")
# password = input("请输入密码")
# if  username == user[0] and password == user[1]:
#     print("登录成功")
#     user[1]="123456"
    



# else:
#     print("账号或密码错误,不允许修改密码")





#马赛克屏蔽器

keywords = ["小明","小红","小绿","小蓝"]
a = input("请输入一句话：")
if keywords[0] in a:
    new_keys =a.replace(keywords[0],"***")
elif keywords[1] in a:
    new_keys =a.replace(keywords[1],"***")
elif keywords[2] in a:
    new_keys =a.replace(keywords[2],"***")
elif keywords[3] in a:
    new_keys =a.replace(keywords[3],"***")
print(new_keys)
