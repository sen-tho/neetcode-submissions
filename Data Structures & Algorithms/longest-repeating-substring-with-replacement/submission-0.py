class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        maxf = 0
        l = 0
        # while length of substring (r-l+1) - max freq > k:
            # freq[s[l]] = freq.get(s[l]) - 1
            # l += 1
            
        for r in range(len(s)):
            # increase frequency of char
            freq[s[r]] = freq.get(s[r], 0) + 1

            # get the maxf with existing maxf value and the freq of the current char
            maxf = max(maxf, freq[s[r]])

            while r - l + 1 - maxf > k:
                freq[s[l]] = freq.get(s[l]) - 1
                l += 1
            
            res = max(res, r - l + 1)

        return res
            
