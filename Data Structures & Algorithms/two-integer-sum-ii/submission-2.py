class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        #   l        r
        # [-2,-1,0,1,2] target 3
        while l < r:
            while numbers[r] > target - numbers[l]:
                r -= 1
            while numbers[l] < target - numbers[r]:
                l += 1
            if numbers[l] + numbers[r] == target:
                return [l + 1,r + 1]

