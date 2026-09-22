class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        result_flag = False
        s_len = len(s)
        for i in range(s_len-1):
            if abs(int(s[i]) - int(s[i+1])) <= 2:
                result_flag = True
            else:
                result_flag = False
                return result_flag
        return result_flag
                

        