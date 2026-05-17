class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map_sum = {}
        
        for i,num in enumerate(nums):
            if (target - num) in map_sum:
                return [map_sum.get((target - num)),i]
            else:
                map_sum[num] = i
        
        return [-1,-1]