"""
Psuedocode:

Loop through nums, use Hashmap to store key : value pairs -> num : frequency in the array 


"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsToFreqDic = defaultdict(int)
        freqArr = [[] for i in range(len(nums) + 1)]

        for num in nums: 
            numsToFreqDic[num] += 1

        for value,freq in numsToFreqDic.items():
            freqArr[freq].append(value) 

        res = []
        for i in range( len(freqArr)-1, 0, -1):
            for value in freqArr[i]:
                res.append(value)
                if( len(res) == k ):
                    return res