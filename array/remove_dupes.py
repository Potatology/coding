


def removeDupes(arr):

    slow = 0  
    for fast in range(len(arr)):
        if arr[fast]!=arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return arr[:slow+1]

print(removeDupes([1,2,3,4,4,4]))