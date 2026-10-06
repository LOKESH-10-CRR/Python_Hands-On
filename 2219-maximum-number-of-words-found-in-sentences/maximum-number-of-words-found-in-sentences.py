class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_len = -10**9
        for sentence in sentences:
            max_len = max(len(sentence.split(" ")), max_len)
        return max_len         