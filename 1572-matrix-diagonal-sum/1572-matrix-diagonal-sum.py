class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        rows=len(mat)
        cols=len(mat[0])
        ans=0
        for i in range(rows):
            for j in range(cols):
                if(i==j):
                    ans+=mat[i][j]
                elif i+j==cols-1:
                    ans+=mat[i][j]
        return ans

        