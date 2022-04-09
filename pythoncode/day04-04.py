# a = 11
# while a == 11:
#     print(a)
#     break

a = (1,2,3,4,5,6,7,8,9,10)
for i in a:
    if i%2 == 0:
        continue #如果满足if条件，就跳过后面的代码
    print(i)
