"""
1.两数之和  暴力破解
"""
# from typing import List


# def Twosums(nums:List[int],target:int)->List[int]:
#     for i in range(len(nums)):
#         x = nums[i]
#         for j in range(i+1,len(nums)):
#             if target - x == j:
#                 return [i,j]


# ch1 = Twosums(nums=[1,2,3,4,5,6,7,8,9],target=10)

# print(ch1)



"""
解法二,二分查找，针对有序数列   hash查找
"""


"""
删除排序数组中的重复项
"""
# def removeDuplicates(nums):
#     for i in range(len(nums)-1):
#         left,right = 0,1
#         while right<len(nums):
#             if left == right:
#                 right +=1
#             elif left != right:
#                 left +=1
#                 left = right
#     return left
                    


# nums = [1,1,1,2,2,3,4,5,5,5]
# a = removeDuplicates(nums)
# print(a)





# def removeDuplicates(nums):
#         if  len(nums)<2:
#             return 0

#         i = 0
#         for j in range(len(nums)):
#             if nums[i] !=nums[j]:
#                 i+=1
#                 nums[i] = nums[j]
#         return i+1


"""
判断所有的数是否有重复的数
"""

#解法1   通过排序后，若元素相等那他们一定相邻
#时间复杂度：nlogn   空间复杂度：logn
# def is_same(li):
#     li.sort()
#     for i in range(len(li)-1):
#         if li[i] == li[i+1]:
#             return True
        
#     return False

# li = [1,2,3,4,1]

# print(is_same(li))

#解法2  利用set集合中不存在重复值，存在重复值会将重复的值删除一个，因此可以比较转化为集合后与之间的数组的长度
#时空复杂度分别为：n N

# def is_same(li):
#     if len(list(set(li))) != len(li):
#         return True
#     else:
#         return False

# li = [1,2,3,4,1]

# print(is_same(li))


#解法3：就是利用hash表，将元素置为key，元素出现的次数作为值

# def is_same(nums):
#     dic = {}
#     for i in nums:
#             if dic.get(i):
#                 return True
#             dic[i] = 1
#     return False

# li = [1,2,3,4,1]
# print(is_same(li)) 



"""
整数反转
"""
# class Solution:
#     def reverse(self, x: int) -> int:
#         if -10 < x <10:
#             return x
#         str_x = str(x)
#         if str_x[0] != "-":
#             x = int(str_x[::-1])
#         else:
#             x = int(str_x[:0:-1])
#             x = -x

#         if -2**31 <x< 2**31-1:
#             return x  
#         else:
#             return 0


"""

"""



