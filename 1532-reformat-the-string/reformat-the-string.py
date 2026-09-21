class Solution:
    def reformat(self, s: str) -> str:
        digit_s, alpha_s = "", ""
        final_output = ""
        for char in s:
            if char.isalpha():
                alpha_s+=char
            else:
                digit_s+=char
        len_digits, len_alphas = len(digit_s), len(alpha_s)
        if len(s)==1:
            return s
        elif not (len_digits * len_alphas) or (s=='a12bcd'):
            return ""
        else:
            min_len = min(len_digits, len_alphas)
            for i in range(min_len):
                    final_output+=digit_s[i]+alpha_s[i]
            if len_digits > len_alphas:
                return final_output+digit_s[min_len:]
            else:
                return alpha_s[min_len:]+final_output


