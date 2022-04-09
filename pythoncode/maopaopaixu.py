# bubble 冒泡
nums = [10,50,25,64,78,90,100,32,39]
def bubble(nums):
    for i in range(0,len(nums)-1):
        for j in range(0,len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

        print(nums)

bubble(nums)
                                                                          