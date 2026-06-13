class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqArr = [[] for x in range(len(nums)+1)]
        freqToVal = dict()

        for n in nums:
            freqToVal[n] = freqToVal.get(n, 0) + 1
        
        for n, f in freqToVal.items():
            freqArr[f].append(n)

        res = []
        for i in range(len(freqArr)-1, 0, -1):
            freq = freqArr[i]
            while len(freq) > 0:
                res.append(freq.pop())
                if len(res) == k:
                    return res
        
        

