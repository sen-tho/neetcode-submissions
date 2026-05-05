class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create dict to store seen 'num: index'
        # begin looping through nums using for i in range(len(nums)) 
            # if current target - currentNum is in dictionary
                # return [seen[val], i]
            # store key:value pair of num: index in seen dictionary
        # return False

        seen = {}

        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in seen:
                return [seen[dif], i]
            seen[nums[i]] = i
            