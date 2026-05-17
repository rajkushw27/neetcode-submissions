class Solution:
    def climbStairs(self, n: int) -> int:

        cache = [-1]*n

        def dfs(i):
            if i >= n:
                if i==n:
                    return 1
                else:
                    return 0
            cache[i] = dfs(i + 1) + dfs(i + 2)

            return cache[i]

        return dfs(0)