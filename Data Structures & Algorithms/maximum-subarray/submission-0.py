class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        current = 0
        for n in nums:
            current = max(current, 0)
            current +=n
            maxsum = max(maxsum, current)
        return maxsum
