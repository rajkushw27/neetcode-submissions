class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        output = [0] * len(temperatures)

        for index,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i,t = stack.pop()
                output[i] = (index - i)

            stack.append((index,temp))

        return output