class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        number_map = set(nums)
        longest_seq = 0
        count = 0

        for i in range(len(nums)):
            
            if nums[i] - 1 not in number_map:
                count=1
                while (nums[i] + count) in number_map:
                    count += 1

            longest_seq = max(count,longest_seq)

    
        return longest_seq
