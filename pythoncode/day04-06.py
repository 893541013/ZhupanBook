# 九九乘法表 for循环

#冒泡排序
# num_list = [11,1,2,33,25,68,99,35,64,55]
# for i in range(len(num_list)):
#     for j in range(i+1,len(num_list)):
#         if num_list[i] > num_list[j]:
#             temp = num_list[i]
#             num_list[i] = num_list[j]
#             num_list[j] = temp
#         print(num_list)



accounts = [{"username":"xm","password":"123456"},
{"username":"xs","password":"123456"}]
username = input("请输入账号：")
password = input("请输入密码：")
i = 1
for account in accounts:
    if account["username"] == username and account["password"] == password:
        print("登陆成功")
        break
    else:
        if i == len(accounts):
            print("登录失败")
i =i+1 