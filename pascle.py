'''Given an integer numRows, return the first numRows of Pascal's triangle.
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]] '''



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        li = []
        n = 1
        ans=1
        while n <= numRows:
            x=[]
            for i in range(n):
                if i > 0: 
                    ans = ans * (n - i) 
                    ans= ans//i
                x.append(ans)
            n = n + 1
            li.append(x)
        return li    