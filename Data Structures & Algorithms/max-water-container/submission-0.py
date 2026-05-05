"""
Pseudocode:
maxArea = 0

Sliding window with two pointers with left (l) starting at 0, right (r) starting at indice 1.

while left pointer is not equal to end of array
    If right pointer reaches end of array
    -> increment left pointer
    -> set right pointer to be one more than left pointer 
    Iterate through list with right point incrementing one each time
        -> get the max possibly height by obtaining the min of the value at the two pointers 
        -> get current area by using this value to multiply by the difference of the two pointers (r-l)
        -> update maxArea if currentArea is greater than current maxArea maxArea = max(maxArea, currentArea)  
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mArea = 0
        l = 0
        r = 1
        
        while l < len(heights)-1:
            w = r - l
            h = min(heights[l], heights[r])
            mArea = max(mArea, w*h)
            r += 1
            if r == len(heights):
                l += 1
                r = l + 1
        return mArea
            