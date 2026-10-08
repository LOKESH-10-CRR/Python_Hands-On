class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        final_output = []
        len_nums = len(nums)
        if len_nums <=1:
            return nums
        for i in range(len_nums-k+1):
            sub_arr = nums[i:i+k]
            if all(sub_arr[i] + 1 == sub_arr[i+1] for i in range(k-1)):
                final_output.append(sub_arr[-1])
            else:
                final_output.append(-1)
        return final_output
        