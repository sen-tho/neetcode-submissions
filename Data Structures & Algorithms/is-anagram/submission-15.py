class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphaNums = [0] * 26
        for i in range(len(s)):
            alphaNums[ord('a')-ord(s[i])] += 1
            alphaNums[ord('a')-ord(t[i])] -= 1
        
        for n in alphaNums:
            if n != 0:
                return False

        return True


