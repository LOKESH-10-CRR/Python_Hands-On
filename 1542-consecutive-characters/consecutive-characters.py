class Solution:
    def maxPower(self, s: str) -> int:
        left, right, max_len, curr_len = 0, 0, 0, 0 
        len_s = len(s)
        while right < len_s:
            if s[left]==s[right]:
                right+=1
                curr_len+=1
                max_len = max(max_len, curr_len)
            elif s[left]!=s[right]:
                curr_len = 0
                left = right
        return max_len     