class Solution:
    def maxPower(self, s: str) -> int:
        
        ### Approach 1 with two pointers
        
        # left, right, max_len, curr_len = 0, 0, 0, 0 
        # len_s = len(s)
        # while right < len_s:
        #     if s[left]==s[right]:
        #         right+=1
        #         curr_len+=1
        #         max_len = max(max_len, curr_len)
        #     elif s[left]!=s[right]:
        #         curr_len = 0
        #         left = right
        # return max_len
        
        ### Approach 2 with single linear flow
        curr_len, result = 1, 1
        len_s = len(s)
        for i in range(len_s-1):
            if s[i]==s[i+1]:
                curr_len+=1
                result = max(result, curr_len)
            else:
                curr_len =1
        return result

