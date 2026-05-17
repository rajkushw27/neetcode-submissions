class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = set()

        for num in nums:
            if num in output:
                return True
            
            output.add(num)

        return False