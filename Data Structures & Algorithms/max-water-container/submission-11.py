class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        r = len(heights) - 1
        l = 0
        while l < r:
            maxArea = max(min(heights[l], heights[r]) * (r-l), maxArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea