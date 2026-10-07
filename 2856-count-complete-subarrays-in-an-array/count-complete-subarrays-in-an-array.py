class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total = 0
        len_set_nums, len_nums = len(set(nums)), len(nums)
        for i in range(len_nums):
            seen = set()
            for j in range(i, len_nums):
                seen.add(nums[j])
                if len(seen)==len_set_nums:
                    total+=1
        return total
        