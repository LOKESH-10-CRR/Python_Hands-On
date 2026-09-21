from collections import Counter
class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        dt_words1 = Counter(words1)
        dt_words2 = Counter(words2)
        lis_words1 = set([i for i, j in dt_words1.items() if j==1])
        lis_words2 = set([i for i, j in dt_words2.items() if j==1])
        return len(lis_words1&lis_words2)

        