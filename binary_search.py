import re


def binarySearch(lst, key): # a list and a key
    low = 0     # variable declaration
    high = len(lst)-1

    while high >= low:
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1
    return -low-1

nums = [2, 6, 9, 10, 7, 11, 20, 1, 3, 15]
nm = sorted(nums)

num = binarySearch(nm, 11)
print(nm)
print(num)
