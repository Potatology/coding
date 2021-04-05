class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mc = 0
        for c in candies:
            mc = max(mc, c)
        res = [False]*len(candies)
        for i in range(0, len(candies)):
            res[i] = mc <= candies[i] + extraCandies
        return res
            