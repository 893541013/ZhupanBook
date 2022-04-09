"""
时间复杂度：
O(1),o(n),O(n2),o(logn)
o(logn)循环减半的时候会出现这种情况
时间复杂度是用来估计算法运行时间的一个单位
常见的时间复杂度：o(1)<o(logn)<o(n)<o(nlogn)<o(n2)<o(n2logn)<o(n3)


空间复杂度：用来评估算法内存占用大小的单位

"""



"""
递归：函数调用自身，如果没有结束条件的话就会一直调用
递归的两个特点：
调用自身，结束条件
"""

"""
队列：先入先出的数据结构

"""



"""
栈：后入先出的数据结构
"""

# def func(x):
#     if x>0:
#         func(x-1)
#         print(x)


"""
递归算法：汉诺塔问题：实际上是将盘子拆解成两部分，一部分是n-1，另一部分是剩余的一部分
"""

"""
二分查找   python内置函数index（）是线性查找   ，二分查找只针对有序列表
"""
# def binary_search(li,val):
#     left = 0
#     right = len(li)-1
    
#     while left<=right:
#         mid = (left+right)//2
#         if li[mid] == val:
#             return mid
#         elif li[mid]>val:
#             right = mid-1
#         else:
#             left = mid +1
#     else:
#         return None


# li = [1,2,3,4,5,6,7,8,9]
# print((binary_search(li,3)))









"""
排序   排序low b三人组：冒泡排序，选择排序，插入排序
       排序Nb三人组：快速排序，堆排序，归并排序
       其他排序：希尔，计数，基数排序
"""
"""
冒泡排序
时间复杂度  o(n2)
"""     
# def maopao_paixu(li):

#     for i in range(len(li)-1):
#         exchange = False
#         for j in range(len(li)-1-i):
#             if li[j]>li[j+1]:
#                 li[j],li[j+1] = li[j+1],li[j]
#                 exchange = True
#         if not exchange:
#             return li
    
    


# li = [5,6,8,9,3,2,1,4,10]
# print(maopao_paixu(li))


"""
选择排序,每一趟选出最小值，把最小值放入一个新列表，再删除老列表的那个原有最小值
"""
# def SelecSort(li):
#     li_new = []
#     for i in range(len(li)):
#         min_val = min(li)
#         li_new.append(min_val)
#         li.remove(min_val)
#     return li_new

# li = [2,1,3,5,8,4,0]

# print(SelecSort(li))



"""
选择排序 优化解：利用冒牌排序的实现原理，将每一趟的第一个位置的元素记为最小值，
然后与j 比较大小，若j小于我们标记的最小值，则交换位置，然后开启第二趟循环  
时间复杂度o（n2）
"""
# def SelectSort(li):
#     for i in range(len(li)-1):
#         min_loc = i
#         for j in range(i+1,len(li)):
#             if li[j]<li[min_loc]:
#                 min_loc = j
#                 li[j],li[i] = li[i],li[j]
#                 print(li)
#     return li

# li = [2,1,3,5,8,4,0]

# print(SelectSort(li))     


"""
插入排序：有序区只有一张牌，每次从无序区选择一张牌把它加入有序区并放入正确的位置
#时间复杂度  o(n2)
"""

# def InsertSort(li):
#     for i in range(1,len(li)):
#         tmp = li[i]   #表示摸到的牌的下标，因为需要做移动所以用一个tmp变量存起来
#         j = i-1   #这里表示手里的牌的下标
#         while j>=0 and li[j]>tmp:
#             li[j+1] = li[j]
#             j-=1
#         li[j+1] = tmp
#     return



"""
三个low b 排序：冒泡排序，选择排序，插入排序 的时间复杂度都是o（n2）
都是原地排序
"""

"""
快速排序：快
快速排序思路：取第一个元素p然后让它归位：让它左边的元素都比他小，右边的元素都比他大
然后再依次看左边的剩余元素，再取左边的第一个元素让他归位，再看左边元素+1个位置的元素
让它也归位，以此类推，右边也是如此

快速排序代码实现
快速排序的时间复杂度：O(nlogn)
快速排序的问题：递归：递归最大深度的问题，递归消耗很多系统资源，无法解决
快速排序会有最坏情况出现：最坏时间复杂度：O(N2)
"""
# def position(li,left,right):
#        tmp = li[left]
#        while left < right:
#               while left<right and li[right]>=tmp:
#                      right -=1
#               li[left] = li[right]
#               while left<right and li[left]<=tmp:
#                      left +=1
#               li[right] = li[left]
#        li[left] = tmp   #这里把tmp归位是为了后续递归
#        return left   #这里返回left或者right的值都可以，是为了下一步左递归去实现左右两边未排序的递归

# def Quick_Sort(li,left,right):
#        if left<right:
#               mid = position(li,left,right)
#               Quick_Sort(li,left,mid-1)
#               Quick_Sort(li,mid+1,right)

# li = [5,6,7,1,2,9,8,10]
# Quick_Sort(li,0,len(li)-1)
# print(li)


"""
深拷贝与浅拷贝：浅拷贝只会复制对象本身，深拷贝则会复制对象本身以及他关联的对象
深拷贝会带来两个问题，一个是一个对象如果调用了他自身，他会无休止地递归拷贝，二是：
"""
"""
快速排序实现2
"""

"""
树的基本概念：由n个节点组成的集合
根节点    叶子节点：叶子节点表示没有分叉的树枝，意思就是没有孩子的节点

树的深度：这个树有几层他就有多少深度

树的度：这个数中最大的节点的个数就代表整个树的深度
孩子节点：父节点：都是相对于来说的
子树：整个树的一个分支

二叉树：每个节点最多往下分两个叉


满二叉树：
所有节点的子节点都是2 的输

完全二叉树：
就是在满二叉树的基础上从右往左摘走几个，左边中不能少



"""

"""
堆排序：基于二叉树，二叉树的表现形式：顺序存储方式（列表）
二叉树：父节点和左孩子节点的关系是：父亲节点为i，左孩子节点为2i+1
右孩子为2i+2

假设孩子节点为i，父亲节点则是i-1//2

堆：是一种特殊的完全二叉树
大根堆：一个完全二叉树，满足任一节点都比其孩子节点大
小根堆：一个完全二叉树，满足任一节点都比其孩子节点小
堆的向下调整：如果节点的左右子树都是一个堆，但树本身不是一个堆，那么通过向下调整来将其变换成一个堆
构造堆：“农村包围城市，从最后一个有孩子的节点开始看”
"""

"""
向下调整的实现：首先建立一个堆：
1.建立一个堆2.得到堆定元素，为最大元素3.去掉堆顶，将最后一个元素放到堆定，进行一次调整重新
使堆有序4.堆定元素为第二大元素5.重复步骤3使堆变为空
"""
# def sift(li,low,high): #向下调整的方法
#        """
#        li:列表
#        low：堆定的位置
#        high：堆的最后一个元素的位置，为什么是high呢？防止向下调整的时候越界
#        """
#        i = low
#        j = 2*i+1
#        tmp = li[low]
#        while j <=high:
#               if j +1 <= high and li[j+1]>li[j]:
#                      j =j+1
#               if li[j] > tmp:
#                      li[i] = li[j]
#                      i = j
#                      j = 2*i+1
#               else:
#                      li[i] = tmp
#                      break
#        else:
#               li[i] = tmp

# def haep_sort(li):  #构造堆
#        n = len(li)
#        for i in range((n-2)//2,-1,-1):
#               sift(li,i,n-i)


# li = [i for i in range(100)]
# import random
# random.shuffle(li)
"""
堆排序的时间复杂度：nlogn
"""

"""
堆的内置模块  实现堆排序
"""
# import heapq   # q ->queue 优先队列（小的先出，大的先出都可以）
# import random
# li = list(range(100))
# random.shuffle(li)
# print(li)

# heapq.heapify(li)   #建堆

# heapq.heappop(li)

# n = len(li)
# for i in range(n):
#        print(heapq.heappop(li),end= ',')


"""
topk问题  类似微博热搜榜  现有n个数，设计算法得到前k大的数（n<k）
解决思路：排序后切片 O（nlogn）+k
排序LOWb三人组：O(kn)
堆排序的思路：O(nlogk)
"""
# def sift(li,low,high): #向下调整的方法
#        """
#        li:列表
#        low：堆定的位置
#        high：堆的最后一个元素的位置，为什么是high呢？防止向下调整的时候越界
#        """
#        i = low
#        j = 2*i+1
#        tmp = li[low]
#        while j <=high:
#               if j +1 <= high and li[j+1]>li[j]:
#                      j =j+1
#               if li[j] > tmp:
#                      li[i] = li[j]
#                      i = j
#                      j = 2*i+1
#               else:
#                      li[i] = tmp
#                      break
#        else:
#               li[i] = tmp



# def TopK():




# def haep_sort(li):  #构造堆
#               n = len(li)
#               for i in range((n-2)//2,-1,-1):
#                      sift(li,i,n-i)


# li = [i for i in range(100)]
# import random
# random.shuffle(li)



"""
归并排序
如果一个列表分成两段有序的列表，然后对左边部分最小的元素和右边最小的元素进行归并：就是比较大小
将较小的元素放入一个临时的列表Ltmp
时间复杂度：nlogn
空间复杂度：n
python内部的sort方法是基于归并排序的
"""

# def merge(li,low,mid,high):
       
#        i = low
#        j = mid+1
#        ltmp = []
       
#        while i <= mid and j<=high:
#               if li[i]<li[j]:
#                      ltmp.append(li[i])
#               else:
#                      ltmp.append(li[j])
#        while i <= mid:
#               ltmp.append(li[i])
#               i +=1
#        while j <= high:
#               ltmp.append(li[j])
#               j +=1
#        li[low:high+1] = ltmp #重新将ltmp写回li列表里面，方便做递归
# def merge_sort(li,low,high):
#        if low<high:
#               mid = (low+high) //2
#               merge_sort(li,low,mid)
#               merge_sort(li,mid+1,high)
#               merge(li,low,mid,high)


# li = list(range(16))
# import random
# random.shuffle(li)
# print(li)
# merge_sort(li,0,len(li)-1)
# print(li)
"""
排序的稳定性：当两个元素值一样的时候保证她们的相对位置不变
稳定性怎么记忆：挨个换的排序是稳定的：冒泡排序，
"""




"""
希尔排序：是一种分组插入排序，原理是：希尔排序每一趟并不使某些元素有序，而是使整个列表趋近于越来越有序
最后一趟使得所有元素有序  最后一趟元素间隔d = 1
时间复杂度N2,gap选择会导致不一样得时间复杂度

"""
# def insert_sort_shell(li,gap):
#        for i  in range(gap,len(li)):
#               j = i-gap
#               tmp = li[i]
#               while j >=0 and li[j] > tmp:
#                      li[j+gap] = li[j]
#                      j -=gap
#        li[j+gap] = tmp

# def shell_sort(li):
#        d = len(li) //2
#        while d >=1:
#               insert_sort_shell(li,d)
#               d //= 2

"""
生成器：调用一次生成一次，节省内存空间   特点：边执行边运算
a = （x for x in range(10)）
next()方法调用生成器
迭代器：
"""

"""
计数排序   enumrate 同时获取下标和值 枚举
0-100之间的数生成1000次并排序
"""
# def count_sort(li,max_count = 100):
#        count = [0 for _ in range(max_count+1)]
#        for val in li:
#               count[val] +=1
#        li.clear()
#        for ind,val in enumerate(count):
#               for i in range(val):
#                      li.append(ind)
# import random
# li = [random.randint(0,100) for _ in range(1000)]
# print(li)
# count_sort(li)
# print(li)


"""
桶排序 时间复杂度：
"""
# def bucket_sort(li,n = 10,max_num = 100):
#        buckets = [[] for _ in range(n)] # 创建桶
#        for var in li:
#               i = min(var//(max_num // n),n-1) # i 表示将数据放入哪一个桶
#               buckets[i].append(var)
#               for j in range(len(buckets[i])- 1,0,-1):
#                      if buckets[i][j] < buckets[i][j-1]:
#                             buckets[i][j],buckets[i][j-1] = buckets[i][j-1],buckets[i][j]
#                      else:
#                             break

#        sorted_li = []
#        for buc in buckets:
#               sorted_li.extend(buc)
#        return sorted_li

# import random
# li = [random.randint(0,100) for i in range(100)]
# # print(li)
# li = bucket_sort(li)
# print(li)

"""
排序练习题
"""
# def two_sum(li,target):
#       for i in range(0,len(li)-1):
#              x = li[i]
#              for j in range(1,len(li)-1):
#                     if x == target -li[j]:
       
#                      return i,j
# li  = [1,2,3,1,2]
# li = two_sum(li,3)
# print(li)



"""
数据结构基础 按照逻辑结构分类：线性结构，树结构，图结构
线性结构：数据结构中的元素存在一对一的相互关系
树结构：数据结构中的元素存在一对多的相互关系
图结构：数据结构中的元素存在多对多的相互关系
"""
"""
列表在python中是怎么存储的？顺序存储   列表也叫顺序表
数组 跟列表有两点不一样：1：数组元素类型要相同2：数组长度固定
列表中存的是地址，通过地址去访问元素
32位机器上一个整数占四个字节，一个地址占四个字节
64位机器上一个整数占8个字节，一个地址占8个字节
查找对于列表来说是O1的时间复杂度
插入和删除对于列表来说是On的复杂度
python的列表是怎么实现的？


"""       
"""
栈：后进先出的数据结构
使用一般的列表即可实现
进栈：li.append
出栈：li.pop
取栈顶：li[-1]

括号匹配问题：
"""
# class Stack:
#        def __init__(self):
#               self.stack = []
#        def push(self,element):
#               self.stack.append(element)
#        def pop(self):
#               return  self.stack.pop()
#        def get_top(self):
#               if (self.stack)>0:
#                      return self.stack[-1]
#               else:
#                      return None
#        def is_empty():
#               return  len(self.stack) == 0

# def barce_math(s):
#        stack = Stack()  #创建栈
#        math = {')':'(',']':'[','}':'{'}
#        for ch in s:
#               if ch in ['(','[','{']:
#                      stack.push(ch)
#               else:
#                      if stack.is_empty():
#                             return False
#                      elif stack.get_top() == math[ch]:
#                             stack.pop()
#                      else:
#                             return False
#        if stack.is_empty():
#               return True
#        else:
#               return False


"""
队列   remove 针对元素   pop 针对下标  队列的实现方式：环形队列   小的数对大的数取余，余数是小的数本身
"""
# class Queue:
#        #创建一个环形队列
#        def __init__(self,size = 100):
#               self.queue = [0 for _ in range]
#               self.size = size
#               self.front = 0  #队手指针
#               self.rear =0     #队尾指针
#        def push(self,element):
#               if not self.is_failed:
#                      self.rear = (self.rear + 1) % self.size
#                      self.queue[self.rear] = element
#               else:
#                      raise IndexError("queue is failed")
#        def pop(self):
#               if not self.is_empty:
#                      self.front = (self.front+1) % self.size
#                      return self.queue[self.front]
#               else:
#                      raise IndexError("queue is empty")
#        #判断队空
#        def is_empty(self):
#               return self.rear == self.front
#        #判断队满
#        def is_failed(self):
#               return self.front == (self.rear + 1) % self.size

"""
python 中队列的内置模块
双向队列：两端都支持进队和出队   queue这个模块是用来保证线程安全的
collections 模块里的 queue包 是一个自动出队的队列
"""
# from collections import deque
# #单向队列：
# # q = deque([1,2,3,4,5])
# # q.append(6)
# # q.popleft(1)

# #双向队列：
# # q = deque([1,2,3,4,5,6])
# # q.appendleft(6)  #队首进队
# # q.pop()   #队尾出队

# def tail(n):
#        with open('text.txt','r') as f:
#               q = deque(f,n)
#               return q

# for line in tail(5):
#        print(line,end="")


"""
链表 ： 头插法  尾插法   链表的创建和遍历
链表的插入和删除
链表对于顺序表来说 按元素查找和按下标查找 复杂度一样 都是On
但是插入和删除操作来说，链表的时间复杂度为O1，列表的时间复杂度为On
所以链表在插入和删除上速度明显快于列表

"""
# class Node:
#        def __init__(self,item):
#               self.item = item
#               self.next = None


# #头插法
# def create_linklist_head(li):
#        head = Node(li[0])
#        for element in li[1:]:
#               node = Node(element)
#               node.next = head
#               head = node
#        return head
# #尾插法
# def create_linklist_tail(li):
#        head = Node([li[0]])
#        tail = head
#        for element in li[1:]:
#               node = Node(element)
#               node.next = tail
#               tail = node
#        return head


"""
hash表：是一个通过哈希函数来计算数据存储位置的数据结构，是一种线性的存储结构
直接寻址表的优点：增删改查速度，非常快
缺点：当存放key的域很大时，比如：key有很多，无限的时候，那么消耗内存非常夸张，很不实际
假如域很大，key很少，浪费大量空间
如果key不是数字而是一个字符串就没法查询了

所有我们引入了哈希函数，直接寻址表+哈希函数 = 哈希表
除法哈希：假设有一个长度为7的哈希表，哈希函数 = h（k）%7
乘法哈希：
全域哈希：
元素集合{14：，22：，3：，5：}

由于hash表大小时有限的，所以哈希冲突是一定会存在的，两个key通过映射都到了一个元素位置上，这个就叫哈希冲突

解决哈希冲突：拉链法  同一位置出现两个key那么用链表将这两个key连接起来
__repr__
return “<<” + ",".join(map(str,self)) ">>"   将某种数据类型转换成字符串
集合的特性：不允许重复，一个元素只允许有一个

哈希表的应用：集合 和字典 的底层就是哈希表
哈希表的总结：哈希表是一个很高效的做查找的数据结构
"""

"""
二叉树的遍历
前序遍历：刚开始访问自己，先访问左子树，再放问右子树
中序遍历：刚开始访问左子树，访问完，在访问根，再放问右子树
后序遍历：刚开始访问左子树，在访问右子树，最后访问根
层序遍历：一层一层的遍历，用队列实现
前序遍历和中序遍历，中序遍历和后序遍历能够确定一棵树，但是没有中序遍历确定不了树


二叉搜索树：如果一个树的节点的左子树都比他小，右子树都比他大 那么他就是一颗二叉搜索树
二叉搜索树删除实现：1.叶子节点直接删除2.如果删除的节点只有一个孩子，将此节点的父亲与孩子连接，然后删除该节点
平衡二叉树：
"""
"""
二叉树的实现：
"""
# class BiTreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.lchild = None
#         self.rchild =None

# a = BiTreeNode("A")
# b = BiTreeNode("B")
# c = BiTreeNode("C")
# d = BiTreeNode("D")
# e = BiTreeNode("E")
# f = BiTreeNode("F")
# g = BiTreeNode("G")


# e.lchild =a
# e.rchild = g
# a.rchild = c
# c.lchild = b
# c.rchild = d
# g.rchild = f
# root = e
# print(e.rchild.rchild.data)

# def pre_order(root):
#     if root:
#         print(root.data,end=",")
#         pre_order(root.lchild)
#         pre_order(root.rchild)




# class BiTreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.lchild = None
#         self.rchild =None
#         self.parent = None



# l = [1,2,3,4,5,6,12]
# new_list = list(filter(lambda x:x % 2 == 0,l))
# print(new_list)



























































