"""
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # Time O(N^2)
        # Space in-place
        # method - transpose the 2D array and then flip each row to modify in-place
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(i+1,rows):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(rows):
            matrix[i] = matrix[i][::-1]
        return matrix

l = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().rotate(l))
