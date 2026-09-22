class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:

        n_lis = list(dict.fromkeys(nums))
        for i in n_lis:
            if (nums.count(i) == 1) and (i&1 == 0):
                return i
        return -1
        