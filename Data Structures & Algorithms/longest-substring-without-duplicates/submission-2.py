"""
Sliding window approach using two pointers (left and right)

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        if len(s) == 1:
            return 1
        
        l = 0
        r = 1
        sub = s[0]
        res = 1

        while l < r and r != len(s):
            if s[r] not in sub:
                sub += s[r]
                res = max(len(sub), res)
                r += 1
                print('if statement: substring:', sub)
            elif s[r] in sub and l != r - 1:
                l += 1
                sub = sub[1:]  
                print('elif statement: substring:', sub)
            else:
                r += 1
                print('substring after else:', sub)
        return res
            