class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = {}
        right = {}
        currentSum = 1
        left[0] = 1
        
        [24,12,8,6]
         
        for i in range(1, len(nums)):
            currentSum *= nums[i - 1]
            left[i] = currentSum
        
        currentSum = 1
        right[len(nums) - 1] = 1
        for i in range(len(nums)-2, -1, -1):
            currentSum *= nums[i + 1]
            right[i] = currentSum
        output = []
        
        for i in range(len(nums)):
            output.append(left[i] * right[i])
        return output