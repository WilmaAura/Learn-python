def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide Process
    mid = len(arr) // 2
    left_half = arr[:mid] # mid - 1
    right_half =arr[mid:] 

    # Recursive for each part
    left_half=merge_sort(left_half)
    right_half=merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0,0
    
    # Merge two parts in order
    while left_index < len(left) and right_index < len (right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index +=1
        else:
            result.append(right[right_index])
            right_index += 1
    
    #add any remaining elements on the left side
    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1
    #add any remaining elements on the right side
    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1
    
    return result

arr = [12, 11, 13, 5, 6, 7]
print ("Array yang belum diurutkan:", arr)
sorted_arr = merge_sort(arr)
print ("Array yang telah diurutkan:", sorted_arr)
