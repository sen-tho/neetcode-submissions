class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            # conditions before starting while loop for l and r pointers:
            # now list is sorted, if not first element and previous element matches current:
                # skip (continue) since we dont want duplicates 
            # if n > 0 break since list is sorted no possible values of j (l) and k (r) can sum to 0 since they are going to be greater than 0

            if i > 0 and n == nums[i-1]:
                continue
            
            if n > 0:
                break

            # l is one position after i hence i + 1
            # r is last element in nums 
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < -(nums[i]):
                    l += 1
                elif nums[l] + nums[r] > -(nums[i]):
                    r -= 1
                elif nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res


    

        