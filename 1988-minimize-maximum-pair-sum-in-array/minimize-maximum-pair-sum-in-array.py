class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        max_sum = 0
        while left<right:
            max_sum = max(nums[left]+nums[right], max_sum)
            left+=1
            right-=1
        return max_sum
        