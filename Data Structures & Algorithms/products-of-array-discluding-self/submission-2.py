class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        zero_cnt = 0
        product = 1

        for num in nums:
            if num:
                product *= num
            else:
                zero_cnt += 1
        if zero_cnt>1:
            return [0] * n

        for i,num in enumerate(nums):
            if zero_cnt:
                if num == 0:
                    result[i] = product
            else:
                result[i] = product//num

        return result

