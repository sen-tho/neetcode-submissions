class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initialize set to store seen chars IF and ONLY IF checked first they dont exist in set (no duplicates)
        # sliding window ( 2 pointers ), l and r -> l = 0, r = l + 1
        # while loop with conditional that l < r
            # check if left char is not equal to right char if l = 0


        if len(s) <= 1:
            return len(s)

        seen = set(s[0])
        l, r = 0, 1
        maxLength = 1

        while r < len(s):
            if s[r] not in seen:
                maxLength = max(maxLength, r - l + 1)
                seen.add(s[r])
                r += 1
            elif s[r] in seen:
                if l == r - 1:
                    l = r
                    r = l + 1
                else:
                    seen.remove(s[l])
                    l += 1
        return maxLength





        

        
