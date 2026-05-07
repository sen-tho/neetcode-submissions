class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum = 0
        L = 0
        target = threshold * k
        valid = 0
        for R in range(len(arr)):
            current_sum += arr[R]
            if R - L +1 > k:
                current_sum -= arr[L]
                L+=1
            if R - L + 1 == k:
                if current_sum >= target:
                    valid+=1
        return valid