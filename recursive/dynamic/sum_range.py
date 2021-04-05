class NumArray:
    def __init__(self, nums):
            self.nums = nums

    def sumRange(self, i, j):
        if i < 0 or j > len(self.nums):
            return null
        sum = 0
        for i in range(i, j+1):
            sum += self.nums[i]
        return sum
print(NumArray([1,2,3,4,5,6,7,8]).sumRange(0,2))