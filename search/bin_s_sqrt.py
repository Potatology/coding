def findSqrt(target):
    l,r, bound = 0, target-1, -1
    while l <= r:
        mid = (l+r)//2
        print(mid)
        if mid**2 > target:
            r = mid - 1
        elif mid**2 <= target:
            bound = mid
            l = mid + 1
    return bound

