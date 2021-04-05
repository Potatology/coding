class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(len(nums)//2):
            j = i + n
            res.append(nums[i])
            res.append(nums[j])
        return res