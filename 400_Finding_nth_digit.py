# Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

 

# Example 1:

# Input: n = 3
# Output: 3
# Example 2:

# Input: n = 11
# Output: 0
# Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
 

# Constraints:

# 1 <= n <= 231 - 1
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        base =1
        while n > 9*digit*base:
            n = n- 9*digit*base
            digit = digit+1
            base = base *10
        q,r = divmod(n-1, digit)
        final_digit = str(q+base)[r]
        return int(final_digit)
