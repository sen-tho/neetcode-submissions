class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = defaultdict(list)

        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c)-ord('a')] += 1
            wordDict[tuple(chars)].append(s)
        
        res = []
        for item in wordDict.values():
            res.append(item)

        return res

