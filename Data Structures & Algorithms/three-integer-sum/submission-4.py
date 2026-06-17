class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # Need the list to be sorted so we can determine whether to increment/decrement l and r pointers
        # For loop to iterator over nums via i with two pointers additionally j and k to calculate 3sum, 
        # with r being the end of the list and l being 1 after i 
        for i in range(len(nums)):
            if i == 0 and nums[i] > 0:
                print('early condition hit')
                return res

            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1 
            k = len(nums) - 1
            while j < k:
                target = nums[i] + nums[j] + nums[k]
                if target < 0:
                    j += 1
                elif target > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return res
