class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsDict = defaultdict(list)

        for s in strs:
            alphaVals = [0] * 26
            for c in s:
                alphaVals[ord(c)-ord('a')] += 1
            anagramsDict[tuple(alphaVals)].append(s)
        
        return list(anagramsDict.values())