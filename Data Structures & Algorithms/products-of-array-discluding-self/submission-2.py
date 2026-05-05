class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = 0 
        r = 0

        res = []
        while r < len(nums):
            temp = 1 
            for l in range(len(nums)):
                if l != r:
                    temp *= nums[l]
            res.append(temp)
            r += 1
        return res