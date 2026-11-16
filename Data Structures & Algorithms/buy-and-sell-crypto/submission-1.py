class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        index = 1
        start = prices[0]
        while index < len(prices):
            if prices[index] > start:
                maxProfit = max(maxProfit, prices[index]- start)
            else:
                start = prices[index]
            
            index +=1

        return maxProfit