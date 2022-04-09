# 自带包
- 使用包必须使用import导入
1. OS  操作系统相关的包或者叫库
```python
import os  #操作系统相关的包
a = os.getcwd()
print(a)
os.mkdir(./xiaoxiao)   #创建文件夹的方法，这里的 . 代表这此时的相对路径 
os.remove()


import sys #环境变量相关的包

print(sys.path)  #获取运行时的环境变量


import random #随机数包
random.randint()      # 随机产生某个区间内的数字
random.choice()      # 随机选择一个参数
random.shuffle()    # 打乱顺序


import time
time.sleep()
time.time()    #获取当前时间，时间戳形式存在
time.localtime()   # 获取当前时间

time.strftime(%Y-%m-%d %H-%M-%S,"参数")  #这里的参数 = localtime获取到的时间


from datetime import datetime   # from import 导入datetime包

datetime.now() #获取当前时间，插入数据库的datetime


import json
a = "{'u':'hsmm'}"  
print()

```


# 第三方包
- 大佬开源使用，pip3管理/pip 来下载删除
```python
pip list  
pip install 包名

清华源下载,加快下载速度
pip list

pip3 install pytest -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install pyyaml -i https://pypi.tuna.tsinghua.edu.cn/simple

```



# 自定义包
将文件变成可以导入的模块
例如 创建一个文件 里面有一个方法

如果到外部 运用这个文件中的方法 ，那么就需要通过 from 文件夹名.文件名 import 方法名，
有时候python会强制要求你在自定义包中插入一个__init__的文件
这里的__init__文件的作用：如果需要在导入自定义包的时候需要让他自动执行代码，那么我们就可以在该文件夹下面添加 init 的文件 ，然后导入时会自动执行这个文件里面的方法



# 导入
- 导入方法/类/变量的含义：就是为了引用某些公共的方法/类/变量
通常情况下面，会把这些方法按照作用不同放到不同的文件夹下面，如果我们需要用到这个方法，那么就绪要导入

- py同级导入

from 文件名 import 方法/变量/类

- py不同级的导入

from 文件名.文件 import 方法/变量/类

如果不想一层一层的去导入变量，需要全部导入的话
就直接 import *


