'''Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        li = []
        di = {}
        n = len(nums)
        sz = n // 3
        for i in nums:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        for k, v in di.items():
            if v > sz:
                li.append(k)
        return li
