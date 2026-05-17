class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        

        for i in range(n):
            product = 1
            for j in range(n):
                if i==j:
                    continue
                else:
                    product *= nums[j]
            result.append(product)

        return result

