class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        output = 0
        freq_map = {}
        left = 0
        max_freq = 0

        for right in range(len(s)):
            
            freq_map[s[right]] = 1 + freq_map.get(s[right],0)
            max_freq = max(max_freq,freq_map[s[right]])

            while (right-left+1) - max_freq > k:
                freq_map[s[left]] -= 1
                left += 1
            
            output = max((right-left+1),output)

        
        return output