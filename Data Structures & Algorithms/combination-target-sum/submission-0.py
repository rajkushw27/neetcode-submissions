class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def dfs(index,curr_sum,arr):

            if curr_sum == target:
                result.append(arr[:])
                return
            if index >= len(nums) or curr_sum > target:
                return

            arr.append(nums[index])
            dfs(index,curr_sum+nums[index], arr)
            arr.pop()
            dfs(index+1,curr_sum,arr)
        
        dfs(0,0,[])

        return result