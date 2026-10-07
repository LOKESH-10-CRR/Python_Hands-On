class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        output = 0
        left, curr_sum = 0, 0
        len_arr= len(arr)
        for right in range(len_arr):
            while right-left+1 > k:
                curr_sum-=arr[left]
                left+=1

            curr_sum+=arr[right]
            if ((right-left+1) ==k) and int(curr_sum / k)>=threshold:
                output+=1
        return output
