class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        bracket_map = { ')': '(',']':'[','}':'{'}

        for b in s:
            if b in bracket_map and stack:
                if bracket_map[b] != stack.pop():
                    return False
            else:
                stack.append(b)

        return True if not stack else False