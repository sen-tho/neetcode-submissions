class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i=0
        length = len(numbers)

        while i < length:
            j = i + 1    
            for j in range(length):
                if numbers[j] + numbers[i] == target:
                    return [i+1,j+1]
            i += 1


