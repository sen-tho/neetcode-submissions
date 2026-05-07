class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentSum = 0
        L = 0
        minSize = float('inf')
        for R in range(len(nums)):
            currentSum += nums[R]
            while currentSum >= target:
                length = R - L + 1
                currentSum-=nums[L]
                L+=1
                minSize = min(length, minSize)
        if minSize == float('inf'):
            return 0
        return minSize
                