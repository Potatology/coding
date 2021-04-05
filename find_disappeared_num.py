class Solution:
    def findDisappearedNumbers(self, nums):
        numdict = {k : 0 for k in range(1, len(nums)+1)}
        output = []
        for i in range(0, len(nums)):
            numdict[nums[i]] += 1
        keylist = list(numdict.keys())
        for key in keylist:
            if numdict[key] == 0:
                output.append(key)


    
#print(Solution().fdn([4,3,2,7,8,2,3,1]))