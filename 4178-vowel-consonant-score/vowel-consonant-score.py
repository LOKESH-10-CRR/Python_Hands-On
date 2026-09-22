import re
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        conso_len, vwl_len = 0, 0
        for i in s:
            if i in 'aeiou':
                vwl_len+=1
            elif i in 'bcdfghjklmnpqrstvwxyz':
                conso_len+=1
        if conso_len > 0:
            return vwl_len // conso_len
        else:
            return 0
