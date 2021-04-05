class Solution:
    def sumOfUnique(self, nums):
        rep_ind = []
        sum = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    rep_ind.append(i)
                    rep_ind.append(j)
        for i in range(0, len(nums)):
            if i not in rep_ind:
                sum = sum + nums[i]
        return sum

    def sumofunique_opt(self, nums):
        nums_dict = dict.fromkeys(nums, 0)
        for i in range(0, len(nums)):
            nums_dict[nums[i]] += 1
        print(nums_dict)
        sum = 0
        for i in nums_dict.keys():
            if nums_dict[i] == 1:
                sum = sum + i        
        return sum

print(Solution().sumofunique_opt([1,2,3,4,5]))