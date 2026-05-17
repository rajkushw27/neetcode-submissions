class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def dfs(index,subset):
            if index==len(nums):
                result.append(subset[:])
                return

            dfs(index+1,subset)
            
            subset.append(nums[index])
            
            dfs(index+1,subset)

            subset.pop()

        dfs(0,[])

        return result