a = 10
b = str(a)
print(type(b),b)


c = int(b)
print(type(c),c)


#字符串转换成对应的元组数组字典
a1 = "(1,2,3)"
b1 = "[1,2,3]"
c1 = '{"username":"zp","age":"21","sex":"male"}'
a2 = eval(a1)
b2 = eval(b1)
c2 = eval(c1)
print(type(a2),a2)
print(type(b2),b2)
print(type(c2),c2)
