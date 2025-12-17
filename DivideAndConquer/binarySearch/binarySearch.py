def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If the target found at mid
        if arr[mid] == target:
            return mid
        # If the target on the left
        if arr[mid] > target:
            right = mid - 1
        # If the target on the right
        else:
            left = mid + 1
    # Jika target tidak ditemukan
    return -1

target = 4
arr = [1,2,3,4,5,6,7,8,9]
result = binarySearch(arr, target)

if result !=-1:
    print ('Target:', target, 'ditemukan pada indeks:', result)
else:
    print ('Target:', target, 'tidak ditemukan dalam array')

    