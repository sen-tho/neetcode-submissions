class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        previous_max = (arr[-1])
        for i in range(length-2, -1, -1):
            current_value = arr[i]
            arr[i] = previous_max
            previous_max = max(current_value, previous_max)
        arr[-1] = -1
        return arr
