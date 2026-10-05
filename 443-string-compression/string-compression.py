class Solution:
    def compress(self, chars: list[str]) -> int:
        len_chars = len(chars)
        if len_chars<=1:
            return len_chars
        else:
            fin_str = ''
            so_far_len  = 1
            for i in range(len_chars-1):
                if chars[i]==chars[i+1]:
                    so_far_len+=1
                else:
                    fin_str=fin_str+chars[i]+ ('' if so_far_len <= 1 else str(so_far_len))
                    so_far_len  =1 
            chars[:] = list(fin_str+chars[i+1]+('' if so_far_len <= 1 else str(so_far_len)))
            return len(chars)


        