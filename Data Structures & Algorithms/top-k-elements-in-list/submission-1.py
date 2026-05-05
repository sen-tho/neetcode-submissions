class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqArr = [[] for i in range(len(nums) + 1)] #account for frequency of 0 as well hence the +1
        freqDict = {} # here we store the frequency of each num

        for n in nums:
            freqDict[n] = freqDict.get(n, 0) + 1 # adds 1 to the value of that key in the dictionary, using .get(n ,0) initializes it to 0 if it doesnt return anything
        
        for num, freq in freqDict.items():
            freqArr[freq].append(num)
        
        res = []
        for i in range(len(freqArr) - 1, 0, -1):
            for n in freqArr[i]:
                res.append(n)
                if len(res) == k:
                    return res
