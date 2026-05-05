class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res, numsLen, i = [], len(nums), 0

        while len(res) < numsLen:
            product = 1
            for i in range( numsLen ):
                if i == len(res):
                    continue
                product *= nums[i]
            res.append(product)
        
        return res
