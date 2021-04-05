class Solution:
  def productExceptSelf(self, nums):
    right = [1] * len(nums)
    print(f'right: {right}')
    prod = 1
    for i in range(len(nums) - 2, -1, -1):
      prod *= nums[i+1]
      right[i] = prod
    print(f'right: {right}')
    prod = 1
    for i in range(1, len(nums)):
      prod *= nums[i-1]
      right[i] *= prod
    print(f'right: {right}')
    return right


print(Solution().productExceptSelf([1, 2, 3, 4]))
# [24, 12, 8, 6]