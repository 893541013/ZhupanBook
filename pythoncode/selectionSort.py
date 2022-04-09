def selection(arr):
    for i in range(len(arr)-1):
        index_min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                j = index_min
                arr[j],arr[i]  = arr[i],arr[j]
        return j 



