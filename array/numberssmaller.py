# Given the array nums, for each nums[i] find out how many numbers 
# in the array are smaller than it. That is, for each nums[i] you have 
# to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        temp = sorted(nums)
        mapping = {}
        result = []
        for i in range(len(temp)):
            if temp[i] not in mapping:
                mapping[temp[i]] = i
        for i in range(len(nums)):
            result.append(mapping[nums[i]])         
        return result

print(Solution().smallerNumbersThanCurrent([1,1,2,3,3,4,5]))