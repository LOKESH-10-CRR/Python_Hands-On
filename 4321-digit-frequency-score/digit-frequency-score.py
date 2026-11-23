class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        dt = {}
        final_frequency_score = 0
        while n>0:
            r = n%10
            if r not in dt:
                dt[r]=0
            dt[r]+=1
            n=n//10
        for key, value in dt.items():
            final_frequency_score+=(key*value)
        return final_frequency_score
        