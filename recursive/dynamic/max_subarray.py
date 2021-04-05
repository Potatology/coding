class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        cur_sum = nums[0]
        best_sum = nums[0]
        for i in range(1,len(nums)):
            cur_sum = max(cur_sum + nums[i], nums[i])
            best_sum = max(best_sum, cur_sum)
        return best_sum
    
    def maxSubArray2(self, a):
        if len(a) == 1:
            return a[0]
        maxSum = a[0]
        for i in range(0, len(a)):
            cursum = a[i]
            for j in range(i+1, len(a)):
                cursum+=a[j]
                maxSum = max(cursum, maxSum)
        return maxSum

    def maxSubArray3(self, a):
        if a == []:
            return None
        maxSum = a[0]
        localBest = a[0]
        for i in range(1, len(a)):
            localBest += a[i]
            if localBest > a[i]:
                if maxSum < localBest:
                    maxSum = localBest
            elif localBest < a[i]:
                localBest = a[i]
                if maxSum < localBest:
                    maxSum = localBest
        return maxSum
    
    def maxSubArray4(self, nums):
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            print(f'dp: {dp[i]} and dp i - 1: {dp[i-1]}')
            dp[i] = max(dp[i-1] + num, num)
        return max(dp)

print(Solution().maxSubArray4([-4,20,0,2,-7,3,31]))


#[-4,20,0,2,-7,3,31]
# curS = 22 -7 or -7? 15!
# maxS = 22
