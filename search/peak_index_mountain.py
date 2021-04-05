#   len.nums >= 3
#   nums[0]<nums[1]<...nums[i-1]<nums[i]
#   nums[i]>nums[i+1]>...len(nums) - 1 

def peakIndexInMountainArray(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid-1]<arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid + 1] > arr [mid]:
            low = mid + 1
        elif arr[mid - 1] > arr [mid]:
            high = mid - 1
    return low

print(peakIndexInMountainArray([1,3,4,3,2,1,0]))
