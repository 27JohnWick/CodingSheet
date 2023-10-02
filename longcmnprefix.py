
'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return " "

        frstwrd = strs[0]
        for i in range(len(frstwrd)):
            for wrd in strs[1:]:
                if(i==len(wrd) or wrd[i] != frstwrd[i]):
                    return frstwrd[0:i]
        return frstwrd