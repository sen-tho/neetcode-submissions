class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        currentMax = 0
        globalMax = nums[0]
        currentMin = 0
        globalMin = nums[0]
        for num in nums:
            currentMax = max(currentMax, 0)
            currentMax += num
            globalMax = max(globalMax, currentMax)
            currentMin = min(currentMin, 0)
            currentMin += num
            globalMin = min(globalMin, currentMin)
        if globalMax < 0:
            return globalMax
        else:
            maybeMax = total - globalMin
            return max(maybeMax, globalMax)