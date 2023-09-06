'''You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4'''

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        dup = 0
        B = list(set(A))
        n = len(B)
        total = n * (n + 1) // 2
        actual = sum(B)
        mis = total - actual
        di = {}
        for num in A:
            if num in di:
                dup = num
                break
            else:
                di[i] = 1
        return [dup, mis]






