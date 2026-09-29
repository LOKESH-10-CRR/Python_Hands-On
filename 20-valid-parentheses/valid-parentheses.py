class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            len_s = len(s)
            rep_s = s.replace('[]', '').replace('{}', '').replace('()', '')
            if len_s == len(rep_s):
                return False
            s = rep_s
        return True
        

        