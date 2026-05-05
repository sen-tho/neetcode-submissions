class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join( filter( str.isalnum, s ) ).replace(" ", "").lower()

        rev = ""
        for c in range( len(s) -1, -1, -1):
            rev += s[c]
        
        
        return rev == s