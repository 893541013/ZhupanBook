# import turtle

# turtle.pensize(4)
# turtle.pencolor('red')

# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)

# turtle.mainloop()



# 占位符
# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))
# a = int(input('a='))
# b = int(input('b='))
# print('%d+ %d = %d' % (a ,b , a + b))


# 逻辑运算符 day 02 语言元素


# 圆周长圆面积
# radius = float(input(":请输入圆的半径"))
# perimeter = 3.14 * radius * 2
# area = 3.14 * radius * radius
# print("圆的周长为：%.2f"%perimeter)
# print("圆的面积为：%.2f"%area)


# 用户身份验证

# username = input("请输入账号：")
# password = input("请输入密码：")

# if username == "admin" and password == "123456":
#     print("登陆成功")
# else:
#     print("登陆失败")


# 分支结构,扁平结构

# x = float(input("X = "))
# if x > 1:
#     y = 3 * x - 5
# elif -1 <= x <=1:
#     y =  x + 2
# else:
#     y = 5*x + 3
# print('f(%.2f) == %.2f'%(x,y))



# 学生成绩等级划分

# score = int(input("请输入学生成绩："))

# if score >= 90:
#     grade = 'A'
# elif 80 <= score < 90:
#     grade = 'B'
# elif 70<= score <80:
#     grade = 'C'
# elif 60 <= score < 70:
#     grade = 'D'
# else:
#     grade = 'E'

# print("该学生成绩等级为：",grade)

# 三角形

# a = int(input("请输入边长a："))
# b = int(input("请输入边长b："))
# c = int(input("请输入边长c："))

# if a+b>c and a+c>b and b+c>a:
#     print("该三角形的周长为：%f"%(a+b+c))
#     p = (a+b+c)/2
#     area = (p*(p-a)*(p-b)*(p-c))**0.5
#     print("该三角形的面积为：%f"%(area))
# else:
#     print("无法构成三角形")


# python  当中循环结构 一种是for-in循环，一种是while循环

"""
求1-100的整数之和
"""
# sum = 0
# for i in range(101):
#     sum += i 
# print(sum)


"""
求1-100之间的偶数之和
"""
# sum = 0
# for i in range(100,1,-2):
#     sum += i
# print(sum)


"""
分支结构求1-100之间的偶数之和
"""

# sum = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         sum += i
# print(sum)


"""
猜数字小游戏
"""

# import random
# from typing import Counter

# answer = random.randint(1,100)
# Counter = 0
# while True:
#     Counter +=1
#     a = int(input("请输入一个数字："))
#     if a > answer:
#         print("大了一点")
        
#     elif a< answer:
#         print("小了一点")
#     else:
#         print("猜对啦")
#         break
# if Counter > 7:
#     print("你的智商余额不够噢")



"""
九九乘法表
"""

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(i,j,i*j),end="\t")
#     print()



"""
输出一个正整数判断是不是素数
条件：首先素数 是只能够被自身整除和被1整除的数，且素数是大于1的
"""
# from math import sqrt

# a = int(input("请输入一个正整数："))
# b = int(sqrt(a))
# is_prime =True
# for x in range(2,b+1):
#     if a%x==0:
#         is_prime = False
#         break
# if is_prime and a!=1:
#     print("%d是一个素数"%(a))
# else:
#     print("%d不是一个素数"%(a))



"""
输入两个正整数，求他们的最大公约数和最小公倍数
python中 / 是除法，返回的是浮点型，//是向下取整

"""

# x = int(input('x = '))
# y = int(input('y = '))
# # 如果x大于y就交换x和y的值
# if x > y:
#     # 通过下面的操作将y的值赋给x, 将x的值赋给y
#     x, y = y, x
# # 从两个数中较的数开始做递减的循环
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break


"""
打印图形，for _ in gange  中的 _ 只是代表占位符，只关注循环的次数，而不是循环的值
"""
# row = int(input("请输入行数："))
# for i in range(row):
#     for _ in range(i+1):        
#         print("*",end="")
#     print()

# row =  int(input("请输入行数："))
# for i in range(row):
#     for j in range(row):
#         if j<row-i-1:
#             print("",end="")
#         else:
#             print("*",end="")
#     print()


"""
等腰三角形？？？？？？？
"""
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()


"""
找到100-1000的所有水仙花数
"""

# for i in range(100,1000):
#     a = i % 10
#     b = i //10%10
#     c = i//100
#     if i == a**3 + b**3+ c**3:
#         print(i)


"""
正整数反转
"""

# a = int(input("请输入正整数："))

# reversed_a = 0      
# while a > 0:
#     reversed_a = reversed_a * 10 + a % 10
#     a //= 10
# print(reversed_a)

"""
字符串反转
"""
# class solution:
#     def reverseString(self):
#         list = [1,2,3,4,5,6,7]
#         for i in range(len(list)//2):
#             list[i],list[len(list)-1-i] = list[len(list)-1-i],list[i]
#         return list



"""
将一颗筛子扔6000次，统计每个点出现的次数

"""

# import random

# f1 = 0
# f2 = 0
# f3 = 0
# f4 = 0
# f5 = 0    
# f6 = 0

# for _ in range(6000):
#     face = random.randint(1,6)
#     if face == 1:
#         f1 +=1
#     elif face ==2:
#         f2+=1
#     elif face == 3:
#         f3 +=1
#     elif face ==4:
#         f4+=1
#     elif face ==5:
#         f5+=1
#     elif face ==6:
#         f6 +=1
# print()


"""
列表的拼接
"""
# list1 = [1,2]
# list2= [1,2,3,4,5,67,8]

# list =list1 + list2

"""
复制整个序列，将两个索引都省略                                      
"""
# print("===============================================================")

"""
摇色子并统计次数?????????
"""
# import random
# counters = [0] * 6
# for _ in range(6000):
#     face = random.randint(1,6)
#     counters[face-1] += 1
# for face in range(1,7):
#        print(f'{face}点出现了{counters[face-1]}次')


"""
list.append    在列表尾部加元素
list.insert（2，xxx）    在列表中按照索引位置加元素
list.remove（）       在列表中删除指定名称的元素
list.pop（2，xxx）     在列表中删除指定索引的元素
list.clear（）        清除列表中的元素
"""


"""
元素的位置和次数
"""
# list = [1,2,3,4,5,5,5,6]
# print(list.index(5))
# print(type(list))
# print(list.index(5))
# print(list.count(5))


"""
元素的排序和反转
sort 进行排序   reverse进行反转
"""


"""
列表的生成表达式，笛卡尔积
"""
# items3 = []
# for x in 'ABC':
#     for y in '12':
#         items3.append(x + y)
# print(items3)

"""
通过生成表达式创建列表
"""
# list1 = [x for x in range(1,10)]

# list2 = [x for x in "hello world" if x not in "aeiou"]

# list3 = [x+y for x in "AB" for y in "123"]


"""
列表的嵌套
"""
# scores = [[0]*3 for _ in range(5)]
# scores[0][0] = 95
# print(scores) 


"""
一元组  ： （100，）要加一个逗号才表示一元组，如果没有逗号就只是表示100这个数组
b = （“hello”）  这个只是单纯表示一个字符串，而不是元组，需要加一个逗号才表示元组
"""


"""
打包解包元组
"""

# a = 1,10,100
# print(type(a),a)    #打包操作
# i,j,k = a             #解包操作
# print(i,j,k)
# 当解包的变量和元组数量不符合时，会报错


"""
星号表达式解决变量数少于元组个数，星号表达式只能出现一次,且 *k会生成一个列表
"""

# a= 1,10,100,1000,10000

# i, j, *k = a
# print(i,j,k)


"""
解包语法对所有的序列成立，也就意味着可以对列表以及我们之前的range函数返回的 范围序列进行解包
"""
# a, b, *c = range(1, 10)
# print(a, b, c)
# a, b, c = [1, 10, 100]
# print(a, b, c)
# a, *b, c = 'hello'
# print(a, b, c)


"""
交换两个变量的值
"""


"""
元组和列表的比较，不可变数据类型在占用内存空间上以及花费的保存时间上优于可变数据类型
"""
# import sys
# import timeit

# a = list(range(100000))
# b = tuple(range(100000))
# print(sys.getsizeof(a), sys.getsizeof(b))    # 900120 800056

# print(timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]'))
# print(timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)'))

"""
元组，列表相互转化
"""
# list = [1,2,3,4,5,6,78,9]
# print(tuple(list))

# tuple = ("1","2","3")
# print(list(tuple))

"""
字符串
"""
# # 字符串s1中\t是制表符，\n是换行符
# s1 = '\time up \now'
# print(s1)
# # 字符串s2中没有转义字符，每个字符都是原始含义，r的作用就是原始化字符串
# s2 = r'\time up \now'
# print(s2)


"""
字符串 == 比较的是字符串的内容，is 则比较的是字符串的内存地址，字符串是不可变类型
"""

# a = 321
# b = 123
# print('{0} * {1} = {2}'.format(a, b, a * b))



# print("hello {}".format("world"))


# a = 321
# b = 123
# print(f'{a} * {b} = {a * b}')


# name = "zhangsan"
# age = "18"
# print(f'我的名字叫{name}，我今年{age}')


"""
字符串的strip方法可以帮我们获得将原字符串修剪掉左右两端空格之后的字符串。
这个方法非常有实用价值，通常用来将用户输入中因为不小心键入的头尾空格去掉，
strip方法还有lstrip和rstrip两个版本，相信从名字大家已经猜出来这两个方法是做什么用的。
"""
# s = '   jackfrued@126.com  \t\r\n'
# # strip方法获得字符串修剪左右两侧空格之后的字符串
# print(s.strip())


"""
变量名.方法名 调用函数
"""
# s = "hello world"
# print(s.replace('o','@'))

"""
拆分合并字符串 split jion,split方法默认按照空格拆分
"""
# s = 'I love you'
# words = s.split()
# print(words)
# print(' '.join(words))


"""
编码解码 encode decode
"""
# a = '我爱你'
# b = a.encode('utf-8')
# c = a.encode('gbk')
# print(b, c) 
# print(b.decode('utf-8'))
# print(c.decode('gbk'))


"""
集和的成员运算的性能要优于列表的成员运算
"""
# set1 = {1,2,3,3,3,4}
# set2 = set(set1)
# print(set2)

# list = [1,2,3,4,5,6,7,7,7]
# set3 = set(list)
# print(set3)

# set4 = {num for num in range(1, 20) if num % 3 == 0 or num % 5 == 0}
# print(set4)

"""
字典   字典中的键必须是不可变类型，字典中的值可以是任意类型
"""
#dict函数
# person = dict(name = "zhangsan",age = "18",sex = "male")
# print(type(person))
#可以通过python的内置函数zip来压缩两个序列形成字典
# item1 = dict(zip("abcde","12345"))
# print(item1)

#字典生成器
# item2 = {x: x**3 for x in range(1,5)}
# print(item2)

# person = {'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号'}
# print(len(person))    # 4
# for key in person:
#     print(key)

# if 'age' in person:
#     person['age'] = 25
# print(person)
# print('tel' in person)


"""
字典的方法
del方法删除元素
pop方法删除字典中对应的键值，并返回该值
stedefalut方法可以增加新的键值对或返回指定的键值对
update方法，使用update更新字典元素，相同的键会用新值覆盖掉旧值，不同的键会添加到字典中
"""
# from _typeshed import SupportsKeysAndGetItem
# from collections import namedtuple
# from math import factorial


# students = {
#     1001: {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'},
#     1002: {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'},
#     1003: {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
# }

# print(students.get(1001))
# print(students.values())
# print(students.keys())

# print(students.items())
# #对字典中的所有键值对进行遍历
# for key,value in students.items():
#     print(key,"---->",value)

# stu1 = students.pop(1001)
# print(stu1)

# stu2 = students.pop(1005,{})
# print(stu2)



# a1 = {
#     1005: {'name': '乔峰', 'sex': True, 'age': 32, 'place': '北京大兴'},
#     1010: {'name': '王语嫣', 'sex': False, 'age': 19},
#     1008: {'name': '钟灵', 'sex': False}
# }
# stu3 = students.update(a1)
# print(students)

# del students(1001)

# print(students)

# stu5 = students.pop(1001,{})
# print(students)

# print(students[1001]['name'])


# person = {'name': '王大锤', 'age': 25, 'sex': True}
# del person['age']
# print(person) 

"""
字典的应用，统计出现过的英文字母次数
"""

# sentence = input('请输入一段话: ')
# counter = {}
# for ch in sentence:
#     if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
#         counter[ch] = counter.get(ch, 0) + 1
# for key, value in counter.items():
#     print(f'字母{key}出现了{value}次.')


# stocks = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }

# stocks2 = {key:value for key,value in stocks.items() if value>100}
# print(stocks2)


"""
函数
"""
# from random import randint
# def roll_dice(n=2):
#     total = 0
#     for _ in range(n):
#         total +=randint(1,6)
#     return total

# print(roll_dice())

# print(roll_dice(3))


"""
可变参数 *arg 以元组的形式出现   命名参数 *kwargs 以键值对的形式出现在最后一行
函数名冲突，不同的模块调用   相同函数名的函数
同时使用两个模块的相同函数名的函数 我们要自己用as关键字对导入的函数进行别名
"""
# from module1 import foo as f1
# from module2 import foo as f2

# f1()
# f2()


"""
生成验证码的函数
"""
# import random
# import string


# All_CHARS = string.digits+string.ascii_letters
# def YanZhengMa(len=4):
#     return''.join(random.choices(All_CHARS,k=len))
# for _ in range(10):
#     print(YanZhengMa())



"""
一个返回给定文件的后缀名的函数
"""
# from os.path import splitext


# def get_suffix(filename, ignore_dot=True):
#     return splitext(filename)[1][1:]

# print(get_suffix("123.txt"))


"""
构造一个函数判断一个给定的正整数是不是质数   
"""

# def is_prime(num: int) -> bool:
#     """判断一个正整数是不是质数

#     :param num: 正整数
#     :return: 如果是质数返回True，否则返回False
#     """
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return num != 1

# num = int(input("请输入一个正整数："))
# print(is_prime(num))


"""
计算两个正整数最大公约数和最小公倍数的函数
"""

# def Max_Gbs_Min_Gys(x:int,y:int)->int:
#     a,b = x,y
#     while b % a != 0:
#         a, b = b % a, a
#     return a, x * y // a

# print(Max_Gbs_Min_Gys(6,5))


"""
去掉整个数例表中的奇数，并计算偶数平方
"""
# number1 = [55,66,22,35,37,36,33]
# number2 = [num **2 for num in number1 if num % 2 ==0]
# print(number2)


"""
映射就是给一个对象（可以是变量、物体、等等）起一个唯一的别名。
例如java中的Map就是一个表达映射的类。
Map names = new HashMap();
names.put("编号9527", "唐伯虎");
这个例子就是把编号9527映射到唐伯虎上，只需要告诉程序你要找编号9527，程序就能找到唐伯虎。这就是映射
"""


"""
装饰器：就是用来装饰函数或类，然后给函数和类添加新的功能，并且他的参数就是函数和类本身
"""
# import random
# import time

# def download(filename):
#     print(f'开始下载{filename}.')
#     time.sleep(random.randint(2, 6))
#     print(f'{filename}下载完成.')

    
# def upload(filename):
#     print(f'开始上传{filename}.')
#     time.sleep(random.randint(4, 8))
#     print(f'{filename}上传完成.')

# start= time.time()   
# download('MySQL从删库到跑路.avi')
# end = time.time()

# start2= time.time()
# upload('Python从入门到住院.pdf')
# end2 = time.time()

# print(f'下载用了{end - start}s')
# print(f'上传用了{end2 - start2}s')
# print(f'总共用了{end - start + end2 - start2}s')


"""
装饰器  ?????????????????????????????????????????????????????????????????????
"""
# import time
# def record_time(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(f'{func.__name__}执行时间: {end - start:.3f}秒')
#         return result

#     return wrapper


# import random
# import time


# def record_time(func):

#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f'{func.__name__}执行时间: {end - start:.3f}秒')
#         return result

#     return wrapper


# @record_time
# def download(filename):
#     print(f'开始下载{filename}.')
#     time.sleep(random.randint(2, 6))
#     print(f'{filename}下载完成.')


# @record_time
# def upload(filename):
#     print(f'开始上传{filename}.')
#     time.sleep(random.randint(4, 8))
#     print(f'{filename}上传完成.')


# download('MySQL从删库到跑路.avi')
# upload('Python从入门到住院.pdf')



"""
用递归函数解决斐波那契数列 == 循环递推  ？？？？？？？？？？？？？？？？？？？？？？？？？？
"""
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a




"""
类和对象
"""
# class Student:
#     """学生"""

#     def __init__(self, name, age):
#         """初始化方法"""
#         self.name = name
#         self.age = age

#     def study(self, course_name):
#         """学习"""
#         print(f'{self.name}正在学习{course_name}.')

#     def play(self):
#         """玩耍"""
#         print(f'{self.name}正在玩游戏.')

# print()

"""
python中给对象发消息有两种方法：也就是调用对象的方法有两种
"""

# # 通过“类.方法”调用方法，第一个参数是接收消息的对象，第二个参数是学习的课程名称
# Student.study(stu1, 'Python程序设计')    # 学生正在学习Python程序设计.
# # 通过“对象.方法”调用方法，点前面的对象就是接收消息的对象，只需要传入第二个参数
# stu1.study('Python程序设计')             # 学生正在学习Python程序设计.

# Student.play(stu2)    # 学生正在玩游戏.
# stu2.play()           # 学生正在玩游戏.


# stu3 = Student()
# Student.study(stu3,'python')
# stu3.study('python')

# stu1 = Student('骆昊', 40)
# stu2 = Student('王大锤', 15)
# stu1.study('Python程序设计')    
# stu2.play()                 



"""
定义一个类描述数字时钟
"""
# import time


# 定义数字时钟类
# class Clock(object):
#     """数字时钟"""

#     def __init__(self, hour=0, minute=0, second=0):
#         """初始化方法
#         :param hour: 时
#         :param minute: 分
#         :param second: 秒
#         """
#         self.hour = hour
#         self.min = minute
#         self.sec = second

#     def run(self):
#         """走字"""
#         self.sec += 1
#         if self.sec == 60:
#             self.sec = 0
#             self.min += 1
#             if self.min == 60:
#                 self.min = 0
#                 self.hour += 1
#                 if self.hour == 24:
#                     self.hour = 0

#     def show(self):
#         """显示时间"""
#         return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'


# # 创建时钟对象
# clock = Clock(23, 59, 58)
# while True:
#     # 给时钟对象发消息读取时间
#     print(clock.show())
#     # 休眠1秒钟
#     time.sleep(1)
#     # 给时钟对象发消息使其走字
#     clock.run()



"""
定义一个类描述平面上的点，要求提供计算到另一个点距离的方法
"""
# class Point:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#     def distance_to(self,other):
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return  (dx * dx + dy * dy)**0.5
#     def __str__(self):
#         return f'({self.x}, {self.y})'


# p1 = Point(3, 5)
# p2 = Point(6, 9)
# print(p1, p2)

# print(p1.distance_to(p2))  #???????????????????????????这一步这个参数P2是什么情况


"""
私有属性 和 受保护属性   __name  私有属性  _name 受保护属性
"""


"""
super函数是python内置的一个初始化父类的函数：super（）.__init__（xxx，xxx）
"""



"""
扑克游戏
python中没有枚举类型，通过继承enum模块的Enum类来实现创建枚举类型
repr 函数 与 str函数的区别：repr面向开发者，更加准确，帮助开发者debug
str 函数面向用户，帮助用户更好的观看代码，阅读代码
"""

# from enum import Enum
# class Huase(Enum):
#     """花色 枚举"""
#     Heitao,Hongxin,Meihua,Fangkuai = range(4)

# for huase in Huase:
#     print(f'{huase}:{huase.value}')

# class Card:
#     def __init__(self,huase,face):
#         self.huase = huase
#         self.face = face
#     def __repr__(self):
#         huases= '♠♥♣♦'
#         faces = ['','2','3','4','5','6','7','8','9','10','J','Q','K','A']
#         return f'{huases[self.huase.value]}{faces[self.face]}'

# card1 = Card(Huase.Heitao,13)
# print(card1)
# Card2 = card(Huase.)



"""
简单选择排序
"""



"""
一个简单的函数用来统计数字/字母出现过的次数
"""

# def counter_math(items):
#     counter = {}
#     for i in items:
#         if isinstance(i,(int,float,str)):
#             counter[i] =  counter.get(i,0)+1
#     return counter


# # ch1 = counter_math([1,1,2,2,3,3,4,5])
# # print(ch1)

# ch2 = counter_math(['a','a','a','b','b','c','c','c','c','c','d','e'])
# print(ch2)



"""
英文句子反转 以及 字母反转
"""




"""
青蛙跳  == 斐波那契数列
"""

# def JumpFloor(n):
#     fn = [1,1]

#     for i in range(n-1):
#         fn[0],fn[1] = fn[1],fn[0]+fn[1]

#     return fn[-1]
# ch1 = JumpFloor(10)
# print(ch1)

"""
hash表
"""



