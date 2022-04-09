def insertionSort(arr):
    for i in range(1,len(arr)):
        current_index = arr[i]
        pre_index = i - 1
        while pre_index>= 0 and pre_index > current_index:
            arr[i],arr[i-1] = arr[i-1],arr[i]
            pre_index -= 1
            arr[pre_index + 1] = current_index
    return arr
            


