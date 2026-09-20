from collections import Counter
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        frequency_count = 0
        dt = Counter(nums)
        for key, val in dt.items():
            if val%k==0:
                frequency_count+=(key*val)
        return frequency_count
        
        