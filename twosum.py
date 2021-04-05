def twoSum(nums, target):
    differenceDict = {}
    for index in range(0, len(nums)):
        diff = target - nums[index]
        if diff in  differenceDict:
            return [index, differenceDict[diff]]
        differenceDict[nums[index]] = index
        

print(twoSum([3,2,4], 6))
