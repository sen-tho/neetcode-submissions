class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)

        maxConsec = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in hashSet:
                runningLength = 1
                temp = nums[i] + 1
                while temp in hashSet:
                    runningLength += 1
                    temp += 1
                maxConsec = max(runningLength, maxConsec)
        return maxConsec