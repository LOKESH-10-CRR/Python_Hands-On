class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        nums1 = (sorted(nums, reverse = True))
        cnt = 0
        for i, j in zip(nums, nums1):
            if i==0 and j!=0:
                cnt+=1
        return cnt