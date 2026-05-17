class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_map = Counter(t)
        s_map = {}
        left = 0
        result, result_length = [-1,-1],float('inf')
        have,seen = 0,len(t_map)

        for right in range(len(s)):
            s_map[s[right]] = 1 + s_map.get(s[right],0)

            if s[right] in t_map and s_map[s[right]] == t_map[s[right]]:
                have += 1

            while have==seen:
                if right-left+1 < result_length:
                    result = [left,right]
                    result_length = (right-left+1)
                
                s_map[s[left]] -= 1
                if s[left] in t_map and s_map[s[left]] < t_map[s[left]]:
                    have -= 1
                
                left += 1

        left,right = result
        return s[left:right+1] if result_length!=float('inf') else ""

