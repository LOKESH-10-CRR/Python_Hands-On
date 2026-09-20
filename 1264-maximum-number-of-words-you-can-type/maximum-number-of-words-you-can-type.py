class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        final_count = 0
        for i in text.split(" "):
            final_count+= int(not set(i)&set(brokenLetters ))
        return final_count
        