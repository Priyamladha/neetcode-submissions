class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        start = 1
        startValue = prices[0]
        while start < len(prices):
            if prices[start] > startValue:
                maxProfit = max(maxProfit, prices[start]-startValue)
            else:
                startValue = prices[start]
            
            start +=1

        return maxProfit