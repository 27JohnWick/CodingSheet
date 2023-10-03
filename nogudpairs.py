'''Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.



Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0'''


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        di = {}
        cnt = 0
        for n in nums:
            if n in di:
                di[n] += 1
            else:
                di[n] = 1
        for count in di.values():
            if count > 1:
                cnt += (count * (count - 1)) // 2

        return cnt


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=len(nums)
        cnt=0
        for i in range(n):
            for j in range(i+1,n):
                if(nums[i]==nums[j]):
                    cnt+=1
        return cnt
