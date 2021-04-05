class Solution:
    def singleNumber(self, nums):
        nummap = {k : 0 for k in nums}
        for i in range(len(nums)):
            nummap[nums[i]] += 1        
        for i in list(nummap.keys()):
            if nummap[i] == 1:
                return i
        return -1






print(Solution().singleNumber([4,1,2,1,2]))