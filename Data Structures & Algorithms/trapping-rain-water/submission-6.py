class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        maxHeightL, maxHeightR = height[l], height[r]
        while l < r:
            if maxHeightL < maxHeightR:
                l += 1
                maxHeightL = max(maxHeightL, height[l])
                res += maxHeightL - height[l]
            else:
                r -= 1
                maxHeightR = max(maxHeightR, height[r])
                res += maxHeightR - height[r]
        return res