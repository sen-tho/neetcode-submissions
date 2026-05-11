class Solution:
    def isPalindrome(self, s: str) -> bool:
        R, L = len(s) - 1, 0
        while R > L:
            if not self.alphanum(s[L]):
                L+=1
                continue
            if not self.alphanum(s[R]):
                R-=1
                continue
            if s[R].lower() != s[L].lower():
                return False
            R-=1
            L+=1
        return True


    def alphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))