'''Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 '''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1=int(a,2)
        n2=int(b,2)
        res=n1+n2
        bin_res=bin(res)
        bin_res = bin_res[2:]
        return bin_res