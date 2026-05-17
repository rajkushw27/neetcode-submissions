class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}
        def dfs(amount):

            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]

            result = float('inf')

            for coin in coins:
                if amount - coin >= 0:
                    result = min(result, 1 + dfs(amount-coin))
            
            cache[amount] = result
            return result
        
        minCoin = dfs(amount)
        return -1 if minCoin == float('inf') else minCoin