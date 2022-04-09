# python的开发环境的搭建
>注意python要使用3.9以上的版本
1.安装python
2.配置环境变量
3.命令行输入 python --version 查看python版本
4.在vscode上面安装python的插件


# python的数据类型
- str
    - 只要用引号引起来的数据就是字符串类型
    - 字符串可以为空
    - \n 表示换行
    - \t 表示缩进

    ```python
    print("123") # 打印字符串
    print("123"+ "456") # 字符串拼接

    ```
- int
    - 只要是整数就是int类型
    - 可以直接对int格式进行加减乘除取余
    - python中的运算符合自然运算的规律
    - 
- float
- bool
    - 浮点类型就是小数类型
    - 浮点型是兼容int的
    - 浮点型和整形可以混合使用，最终结果肯定是浮点型。
- list
- tuple
    - 元组是不可变数据类型，但是元组中的列表是可以修改的

- dict
    - 字典也是一个数据集合，在python中用[]表示
    - python中的字典格式，在其他编程语言中叫对象
    - 字典格式是以键值对形式存在的，key不可变，value可变
    - 字典的key不建议使用非字符串格式
    - 字典的取值，用print（a["key"]）若键不存在，则抛出异常，不太安全
        若用print(a.get("key")) 若key不存在，返回None，较为安全
    - popitem，以元组格式（key，value）的格式去除最后一个数据
    - 
- set
    - 集合是一个无序不可重复的数据结构

# python的常用函数

### print
    - print这个方法可以打印出具体数值
    - print这个方法支持任意数量的数据进行打印
    - print 默认打印的值结尾处 会有一个换行符,我们可以通过控制end参数中等号的后面的值来进行控制是否换行
    ```python
    print(123,end = "")
    print(123,end = "|")
    ```
    - sep参数，print中每个用逗号隔开的数据打印出来之后是用空格隔开，那么sep这个参数也可以控制是否用空格隔开
    ```python
    print("111","222","hahaha")

    
    print("111","222","hahaha",sep = "|")
    ```
    

### input
```python
print(----------------------)
value = input("请输入：")

print("您输入的值是：" + value)
print(----------------------)
``` 
    - input可以让用户在终端输入任何数据
    - input的格式化字符串的两种方式
```python
names = input("请输入你的名字：")
ages = input("请输入你的年龄：")
print("%s的年龄是%s" % names,ages)
print("{}的年龄是{}".format(names,ages))

print("{name}的年龄是{age}".format(name = names,age = ages))
```
具体的用法就是上述三种方式。

### int()
    - 将float转换成整数类型
    - 将长得像数字的字符串转换成整形
###　str()
    - 将任意数据类型转换成字符串
    - 字符串的内键： isdigit，判断字符串是否全是数字
                    isspace，判断字符串是否全为空格
                    title，将字符串的首字母大写
                    upper，将字母小写变为大写打印输出
                    join，
                    split
                    reversed，这个方法可以针对列表， 
                    ```python
                    
                    ```   
###　float()
    - 将int类型转换成浮点类型
    - 将长得像数字的字符串类型转换成浮点型

### type()
    - 获取数据类型

# python的运算符号
- 加
    ```python
    print(123+123)
    ```
- 减
    ```python
    print(123-23)
    ```
- 乘
    ```python
    print(123*23)
    ```
- 除
    ```python
    print(111/11)
    ```
- 余
    ```python
    print(123%23)
    ```
- 幂
    ```python
    print(2**3)
    ```
- 向下取整,向下取整指做完除法后舍去余数，不会进行四舍五入
    ```python
    print(11//2)
    ```
- 模
    取模运算




# python的判断符号
- ==
- ">"
- <
- in
- not in 
- !=
...

# python的判断逻辑连接词
- and，表示并且
- or，表示或者
- and not，表示并且不
- or not，表示或者不

# python的判断条件
- python 的代码块是以缩进来标识的
- python判断的三种处理方式
    - 单独的判断
    ```python
    name = "张三"
    if name == "张三"：
        print("符合条件")
    ```
    - if ...else...的语句
    - if...elif...else的语句，elif写在if和else的中间，可以写多个elif，可以做多次判断
    - isinstance()
        - 这个方法用来快速判断数据类型
        - 下面这个例子可以来判断a是否为int类型，若是，返回ture，否则，返回false
        ```python
        a = "字符串"
        print(isinstance(a,int))
        ```
        - instance的第二种用法可以用来判断数据是否在某个数据类型范围内
        ```python
        a = "字符串"
        print(isinstance(a,(int,str)))
        ```
    - issubclass
# python的循环
- for循环
    - 普通循环
    >for 循环是通过遍历来实现的，遍历的意思将每个数据，挨个数一遍
    - 嵌套循环
    
- while循环
    >while循环是通过条件判断来循环的，只要满足条件，代码会一直运行
    ```python
        a = 1
    while a <10:
        print("第{}次循环".format(a))
        a +=1
    ```
    -break 和 continue在while循环中的作用
    ```python
        a = 1
    while a <12:
        a +=1
        if a % 2 == 1:
            continue
        
        if a == 10:
            break
    ```
    这里我想到一个问题，a在头部累加，那么a = 1是不是就没进入判断了啊？
- 终止循环
```python
a = [1,2,3,4,5,6,7]
for i in a:
    if i ==5:
        break
    print(i)
```
本次循环只会打印1,2，3,4，循环到5的时候因为条件判断，终止本次循环
- 跳过循环
```python
a = [1,2,3,4,5,6,7]
for i  in a:
    if i%2 !=1:
        continue
    print(i)
``` 
这次循环只会打印1,3,5,7，因为定义了循环条件，按照循环条件跳过
- range()
    -range可以自动生成一个任意长度的列表
    ```python
    a = range(10) # range(a,b,c) 里卖弄有三个参数，a参数的用法
    print(list(a)) #生成0-9，第一个参数的用法，从哪里开始生成
    
    a = range(5,10) #range的第二个参数的用法，从第几个数结束，这里会生成5,6,7,8,9

    a = range(9,20,3) #range的第三个参数的用法，步长，隔3个数生成相应的列表

    ```




# Flask 与 Django 的区别
falsk 是一个轻量级的后端框架
django 是一个很庞大的后端框架，很多东西都用不上的















