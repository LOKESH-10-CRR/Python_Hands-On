class Solution:
    def reverseWords(self, s: str) -> str:
        def vowel_counter(st):
            return len([i for i in st if i in 'aeiou'])
        s = s.split(" ")
        vowel_count = vowel_counter(s[0])
        for i in range(1, len(s)):
            if vowel_count == vowel_counter(s[i]):
                s[i] =s[i][::-1]
        return " ".join(s)
        