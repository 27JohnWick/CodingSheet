'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        di = {}
        if (n <= 1):
            return nums[-1]
        for el in nums:
            if el in di:
                di[el] += 1
            else:
                di[el] = 0
        for k, v in di.items():
            if v == 0:
                return k

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
