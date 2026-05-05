""""
*Elements DO NOT have to be consecutive in the original arary

Initialize a counter to 1
Loop through the elements in nums via for loop
Can utilize an unordered set (no duplicates) 
    -> each itereation lookup if previous consecutive value to current number
     in iteration exists
    -> if it does 
        -> increment counter
    -> else doesnt
        -> reset counter to 1
    append number to unordered set  
    
    return counter
    
in store each value

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        res = 0
        for num in numsSet:
            if num -1 not in numsSet:
                length = 1
                while num + length in numsSet:
                    length += 1
                res = max(res, length)
        return res