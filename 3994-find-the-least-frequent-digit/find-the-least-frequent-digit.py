from collections import Counter
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        dt = Counter(str(n))
        digit, freq = min(dt.items(), key=lambda x: (x[1], int(x[0])))
        return int(digit)

        