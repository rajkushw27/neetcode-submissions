class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!= len(t):
            return False

        t_count = [0] * 26
        s_count = [0] * 26

        for ch in t:
            t_count[ord(ch)-ord('a')] += 1
        
        for ch in s:
            s_count[ord(ch)-ord('a')] +=1

        for i in range(26):
            if t_count[i] != s_count[i]:
                return False
        
        return True