class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        len_nums = len(nums)
        for i in range(len_nums-1):
            if nums[i]<nums[i+1]:
                continue
            else:
                return i
                break
        return len_nums-1 if (nums == sorted(nums)) else 0