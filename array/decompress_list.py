class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        if len(nums) % 2 != 0:
            return[]
        res = []
        i = 0
        while i < len(nums):
            sub = [nums[i + 1]] * nums[i]
            res.extend(sub)
            i += 2
        return res
        