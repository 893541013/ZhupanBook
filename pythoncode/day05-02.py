import time
import os
import sys
import random
# time.sleep(5)
# print("123456789")


a = os.getcwd()#获取当前文件在哪个文件夹下面
print(a)

b = sys.path
print(b)

# c = random.randint(1,100000)
# print(c)



userlist = ['a','b','c','d','e','f','g','h','j','k']
countlist = [0,0,0,0,0,0,0,0,0,0,]
for i in range(10):
    d = random.randint(0,len(userlist)-1)
    countlist[d] = countlist[d]+1
print(countlist)


