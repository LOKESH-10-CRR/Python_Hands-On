from collections import Counter
class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        dt_words1 = Counter(words1)
        dt_words2 = Counter(words2)
        final_count = 0
        for i in dt_words1:
            if i in dt_words2 and (dt_words1[i]==1 and dt_words2[i] ==1):
                final_count+=1
        return final_count

        