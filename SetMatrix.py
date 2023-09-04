'''Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row ,col = [0] * len(matrix),[0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row[i],col[j] = 1,1

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0