class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [ c for x in matrix for c in x]

        L, R = 0, len(nums) - 1 

        while L <= R:
            mid = ((R - L) // 2) + L 

            if nums[mid] < target:
                L = mid + 1 
            elif nums[mid] > target:
                R = mid - 1
            else:
                return True
        return False 