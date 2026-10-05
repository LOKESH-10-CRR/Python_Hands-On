from collections import Counter
class Solution:
    def findPairs(self, nums, k: int) -> int:
 
        if k == 0:
            freqs = Counter(nums)
            return sum(freqs[k] > 1 for k in freqs)
   
        sorted_set_list = sorted(list(set(nums)))
        length = len(sorted_set_list)
        slow = 0
        fast = 0
        answer = 0
        while fast < length:
            difference = sorted_set_list[fast] - sorted_set_list[slow]
            if difference < k:
                fast += 1
            elif difference > k:
                slow += 1
            else:
                answer += 1
                slow += 1
                fast += 1
        return answer