def k_largest(arr: list[int], k: int) -> int:
    if k <= 0 or k >= len(arr):
        return None
    # easier to write k as the real position in the array
    k = len(arr) - k

    return k_largest_help(arr, k, 0, len(arr) - 1)

# same as quick select algorithm
def k_largest_help(arr: list[int], k: int, start: int, end: int) -> int:
    pivot = k
    left, right, = start, end

    while left < right:
        while arr[left] < arr[pivot]:
            left += 1
        while arr[right] > arr[pivot]:
            right -= 1

        arr[left], arr[right] = arr[right], arr[left]

        if pivot == left:
            pivot = right
            left += 1
        elif pivot == right:
            pivot = left
            right -= 1
        else:
            left += 1
            right -= 1

    # only sort the partition where k is
    if k > pivot: start = pivot + 1  
    elif k < pivot: end = pivot - 1
    else: return arr[k]
    
    return k_largest_help(arr, k, start, end)

print(k_largest([10, 0, 11, 23, -2], 3))
print(k_largest([9, 1, 9, 2, 9, 3, 9, 4, 9, 5, 9], 4))
print(k_largest([1, 2, 1, 3, 1, 4, 1, 5, 1], 2))
print(k_largest([9, 1, 9, 2, 9, 3, 9, 4, 9, 5, 9], 4)) 
print(k_largest([6, 2, 6, 3, 6, 4, 6, 6, 6, 6], 7))
print(k_largest([4, 1, 4, 2, 4, 3, 4, 5, 4, 4, 4, 4], 9)) 
print(k_largest([2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 2, 2], 4)) 
print(k_largest([5, 1, 5, 2, 5, 3, 5, 4, 5, 6, 5, 7, 5, 8], 6)) 
print(k_largest([5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 5], 5))
print(k_largest([5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4], 0))
print(k_largest([3, 2, 3, 1, 3, 4, 3, 5, 3, 4, 3], 7))
