"""
Psuedocode:
First do a if statement check to ensure character length is same of each string
for if it is not we can immediately return False

Pick a string to iterate through (lets say 's')
    - do an immediate if statement check to see if char doesnt exist in other string 
        because if it doesnt we immediately return false
    - check if char exists in other string 't'
        - if it does remove the first instance of that character via replace(char,"", 1)
    
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        for char in s:
            if char not in t:
                return False
            t = t.replace(char, "", 1)

        if len(t) != 0:
            return False

        return True