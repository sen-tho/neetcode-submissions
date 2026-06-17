class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxWater = 0 

        maxL = 0
        maxR = 0
        while l < r:
            maxL = max(heights[l], maxL)
            maxR = max(heights[r], maxR)

            length = r - l
            maxSharedHeight = min(maxL, maxR)
            area = length * maxSharedHeight

            maxWater = max(maxWater, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater
