# python模块
- pycache__ ：这个文件是我们的缓存文件，当py文件运行之后，python编译器（安装的python包就是python编译器）会把python的py文件转化成pyc文件并放到 paycache文件夹里面

# 方法/类/代码行
- 方法，类，代码行 都可以存放在我们的py文件中，一个py文件可以存放一个or多个方法，类，代码行

# 变量
- 变量是有作用域的


# 类
类是比方法更高级的代码实现方式，可以理解为一个做蛋糕的模板，事先定义好蛋糕，有哪些功能，通过调用模板实现做蛋糕的目的

```python
class Person()
 # 属性：成员变量/实例变量
 name = "zhaozhao"
 age = "18"
 sex = "male"
 job = "测试一枚"
#  成员方法/实例方法

def eat(self):
    print("他可以吃东西")

def drink(self):
    print("他可以喝东西")


# 通过人的类以及人的一些方法我们来实现一个人类
p = Person()

p1 = Person()

# 上面创建好的两个人 能够去调用人类的成员属性和成员变量
print(p.name)
p.eat()
```
- 成员变量
成员变量指的是我们类中的全局变量，可以跨成员方法使用，self.变量
- 成员方法
类中的实例方法，只能用实例对象来调用
实例方法的参数和返回值和普通方法一样，需要注意实例方法的第一个参数永远是self，并且self可以不传参
- self 关键字
self 指的是一个实例对象，与p = Person（）的p对象是一样的
self 只能在类的内部使用，p 就只能在类的外部使用
- self的作用
1.self在内部使用成员变量和方法
2.self可以去修改或者创建新的成员变量
3.self 可以调用其他的成员方法



## 类的继承
- 子类可以继承父类的变量和方法
- 子类也可以重写父类的变量和方法
```python
# 父类
class BaBa:
    name = "马化腾"
    money = "2000E"
  
    def make_money(self):
        print("这家公司叫腾讯")
  
# 子类：继承了父类BaBa
class Son(BaBa):
    name = "小马"
    money = "5000E"
  
    def make_money(self):
        print("这家公司不仅仅只有腾讯，还有阿里， 还有字节")
  

  
son = Son()
# 继承属性和方法
print(son.money)
son.make_money()

# 子类可以继承父类的属性和方法
# 子类可以重写父类的属性和方法

```
## 封装
将方法封装实现成员变量的调用，一般不直接去拿成员变量，而是通过类的内部封装的方法去拿他的成员变量

```python
# 三大特性，多态、封装、继承:实现方式，规范

# 封装
class Test:
    name = "123"
    age = 123
  
    # 方法封装实现成员变量的设置和引用
    def get_name(self):
        return self.name
  
    def set_name(self, v):
        self.name = v
    
t = Test()
t.get_name()
t.set_name("ddddd")

```
## 多态
通俗讲：父类和子类可以有同一个方法，当父类有多个子类时，第二个子类也可以去拿父类的方法来重写，多个子类都可以去拿方法重写

- 重写方法 也叫多态

```python
# 父类:
class BaBa:
    name = "马化腾"
    money = "2000E"

    def make_money(self):
        print("这家公司叫腾讯")

    def dance(self):
        pass


# 子类：继承了父类BaBa
class Son(BaBa):
    name = "小马"
    money = "5000E"

    def make_money(self):
        print("这家公司不仅仅只有腾讯，还有阿里， 还有字节")



son = Son()
# 继承属性和方法
print(son.money)
son.make_money()

```

# 上述三个方式 可以让类的拓展性变得异常优秀

