class Solution:
    def containsDuplicate(self, nums):
        numSet = set()
        for i in range(0, len(nums)):
            if nums[i] in numSet:
                return True
            else: 
                numSet.add(nums[i])
        return False
    
    def containsDuplicate2(self, nums):
        return len(set(nums)) != len(nums)



print(Solution().containsDuplicate2([1,2,3,1]))