


#     #方法:成员方法：类的实例

#     def eat(self,food,foods):
#         print(id(self))
#         xm.name = "xx"
#         self.drink()   #调用成员方法

#         self.width = 120 # 新增成员变量
#         print("{} keyi  chi {},{}".format(self.name,food,foods))
#         return 123
#     def drink(self):
#         print("ta keyi he shenm ")
    
# #实例化
#  #xm：实例化对象：person（）实例化类
# xm = person()
# #实例化对象调用成员方法和成员变量
# print(xm.name)
# print(id(xm))  #id是显示变量的内存地址
# xm.name = "xx"
# a = xm.eat("noodles","tea")
# print(xm.width)


class cat():

    def __init__(self,name):
        self.name = name
cat1 = cat("lihuamao")
print(cat1.name)
cat2 = cat("yingduan")
print(cat2.name)       
        