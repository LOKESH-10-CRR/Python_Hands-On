class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        len_nums = len(nums)

        if len(set(nums)) == 1:
            return len_nums

        left = 0
        mid = len_nums // 2
        right = (len_nums + 1) // 2
        answer_array = 0

        while left < mid and right < len_nums:
            if nums[left] < nums[right]:
                left += 1
                right += 1
                answer_array += 1
            else:
                right += 1

        return len_nums - (2 * answer_array)