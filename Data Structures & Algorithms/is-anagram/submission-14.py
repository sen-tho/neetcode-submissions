class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alphaVals = [0] * 26
        for i in range(len(s)):
            alphaVals[ord('a') - ord(s[i])] += 1
            alphaVals[ord('a') - ord(t[i])] -= 1

        for val in alphaVals:
            if int(val) != 0:
                return False
        
        return True

        

