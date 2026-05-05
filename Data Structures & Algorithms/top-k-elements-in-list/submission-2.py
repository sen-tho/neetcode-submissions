class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqArr = [[] for i in range(len(nums) + 1)]
        count = {}

        for n in nums:
            count[n] = count.get(n,0) + 1
        
        for n, f in count.items():
            freqArr[f].append(n)
        
        res = []
        for i in range(len(freqArr) - 1, 0, -1):
            for n in freqArr[i]:
                res.append(n)
                if len(res) == k:
                    return res