class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = defaultdict(int)
        tcount = defaultdict(int)
        for letter in s:
            scount[letter] +=1
        for letter in t:
            tcount[letter] +=1
        return tcount == scount
