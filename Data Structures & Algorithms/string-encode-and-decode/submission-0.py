class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res, l = "", []

        for s in strs:
            res += str(len(s)) + "#" + s

        print("1st enc RES", res)
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j + length + 1

        return res