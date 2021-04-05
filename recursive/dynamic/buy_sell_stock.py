class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        for buyDay in range(len(prices) - 1):
            for sellDay in range(buyDay + 1, len(prices)):
                currentProfit = prices[sellDay] - prices[buyDay]
                if currentProfit > maxProfit:
                    maxProfit = currentProfit
        return maxProfit

    def maxProfit2(self, prices):
        if len(prices) <= 1:
            return 0
        maxPrice = 0
        maxProfit = 0
        for day in range(len(prices)-1, -1, -1):
            if prices[day] > maxPrice:
                maxPrice = prices[day]
            if maxProfit < maxPrice - prices[day]:
                maxProfit = maxPrice - prices[day]
        return maxProfit
    def maxProfit3(self, prices)
        if len(prices) <= 1:
            return 0
        maxPrice = 0
        maxProfit = 0
        for price in prices[::-1]:
            maxPrice = max(price, maxPrice)
            maxProfit = max(maxProfit, maxPrice - price)
        return maxProfit        
print(Solution().maxProfit2([7,1,5,3,6,4]))