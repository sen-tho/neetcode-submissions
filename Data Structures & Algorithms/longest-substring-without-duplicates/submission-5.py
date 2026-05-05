class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initialize set to store seen chars IF and ONLY IF checked first they dont exist in set (no duplicates)
        # sliding window ( 2 pointers ), l and r -> l = 0, r = l + 1
        # while loop with conditional that l < r
            # check if left char is not equal to right char if l = 0
        seen = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            seen.add(s[r])
        return res





        

        
