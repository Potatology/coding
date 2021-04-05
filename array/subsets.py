def subsets(nums):
    if nums == []:
        return []
    
    powerset = [[]]

    for num in nums:
        for i in range(len(powerset)):
            copysub = powerset[i].copy()
            copysub.append(num)
            powerset.append(copysub)    
    return powerset

print(subsets([1,2,3]))