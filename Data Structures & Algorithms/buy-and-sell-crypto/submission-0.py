class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = float('inf')
        result = float('-inf')

        for price in prices:
            low = min(low,price)
            profit = price - low
            result = max(result,profit)

        return result
