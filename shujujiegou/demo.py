# print("123" + "456")

# print("123" + "456")



# print("".join(reversed("abc")))



# 元组




# 集合

# a = {"zhang","li","wang"}
# b = {"zhang","li","liang"}
# print(a - b)
# print(a | b)
# print( a & b)


# python的判断条件

"""
登陆条件判断
"""
# username = input("请输入你的账号")
# password = input("请输入你的密码")
# if username == "root" and password =="123456":
#     print("登陆成功")
# else:
#     print("登录失败")

"""
多重判断
"""
# age = int(input("请输入你的年龄："))
# if age <12:
#     print("你还小")
# elif 12<= age <20:
#     print("你还是不够大")
# elif 20<= age <30:
#     print("或许你已经够大了 ")
# else:
#     print("你超龄了")


# print(isinstance(age,(int,str)))


# a = [1,2,3,4,5,6,7]
# for i  in a:
#     if i%2 !=1:
#         continue
#     print(i)


# a = [1,2,3,4,5,6,7]
# for i in a:
#     if i ==5:
#         break
#     print(i)


# a = range(100)
# print(list(a))


# while循环
# a = 1
# while a <12:
#     a +=1
#     if a % 2 == 1:
#         continue
    
#     if a == 10:
#         break
    
#     print("第{}次循环".format(a))


#1. try > 报错了 >except >finally


# try:
#     a = [1,2,3]
#     print(-100)
# except Exception as e:
#     print(e)
#     print("报错了")
# else:
#     print("没有报错")
# finally:
#     print("finally")



# python的内置方法和内置变量的使用

# python对每个py文件，方法，类都是由内置变量的方便获取关于代码的一些基础信息

# py







# from functools import reduce, wraps

# def test(s1,s2):
#     return s1+s2

# reduce(test,[1,2,3,4,5])   #注意reduce不是for循环，第一个参数是test，第二个参数是一个可序列化的参数

# from functools import partial

# def test1(s1,s2):
#     return s1+s2

# add = partial(test1,1)
# # add 变成了
# # def test2（s2）：
# #    return 1+s2

# #print（add（100，200））   # 此时就多传入了一个参数 typeerror
# print(add(100))



from functools import wraps
def a(f):
    # wraps 的参数f实际上是被装饰函数，这个前面装饰器的调用链路就可以得知
    @wraps(f)    # wraps 实际上的底层方法就是partial，通过partial函数来帮顶原有的内置属性，以此保证被装饰器的函数不受影响
    def b(*args,**kwargs):
        print("b")
        return f()
    return b

@a
def t():
    print("t")

print(t.__name__)  #这里不用wraps 消除装饰器对被装饰函数的内置属性的修改的话
#应该打印的是 b

#经过被装饰后的函数，它的内置属性已经改变了，并不是在运行被装饰函数，实际上
# 在运行装饰器函数里面生成的原函数的副本
# 一个函数被装饰之后，实际上他就已经改变了，wraps方法就是在消除这种影响








    
    
