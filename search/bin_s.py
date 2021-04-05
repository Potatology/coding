def binarySearch(nums, target):
    high = len(nums)-1
    low = 0
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1
print(binarySearch([1,2,3], 4))