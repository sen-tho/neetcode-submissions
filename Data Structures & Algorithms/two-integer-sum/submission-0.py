"""
Psuedocode:
- Initialize empty dictionary to store key value pairs of num: indice 

- for loop in range iterating list of nums
    - lookup if target - current num is IN dicitonary 
        - if true, return [ indice of corresponding num in dictionary, current i ]
    - else 
        - store key value pair of number in dictionary
    
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storedNums = {}

        for i in range(len(nums)):
            dif = target - nums[i]

            storedNumExist = storedNums.get(dif, False)
            print("StoredNumExist", storedNumExist)

            if storedNumExist:
                return [int(storedNumExist), i]
            
            storedNums[nums[i]] = str(i)
        return []