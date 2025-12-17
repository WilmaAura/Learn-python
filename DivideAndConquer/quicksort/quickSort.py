def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot]
    
    return quickSort(left) + mid + quickSort(right)
arr = [12,11, 3, 21, 41]
print ("len arr:",len(arr))
print ("Before sorted:",arr)
sorted = quickSort(arr)
print ("After Sorted:", sorted)