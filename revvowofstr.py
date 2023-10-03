
'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"

'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        li = []
        for ch in s:
            if ch in vowels:
                li.append(ch)
        res = []
        for ch in s:
            if ch in vowels:
                res.append(li.pop())
            else:
                res.append(ch)

        return ''.join(res)
