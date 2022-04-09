class Baba():
    name = 'mayun'
    money = '1000e'
    def make_money(self):
        print("wo zui houhui de shiqing jiushi chuangjian l alibaba")
# son类 继承 baba 类
class Son(Baba):
    name = 'xiao ma yun '
    money = '5e'
    def make_money(self):
        print("wo zui kaixin de shiqing jiushi chuangjian l pinduoduo")
#子类 可以继承 父类的变量和方法
Son = Son()
print(Son.money)
Son.make_money()

# 子类可以重写父亲类的属性和方法
