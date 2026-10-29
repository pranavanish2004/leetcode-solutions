class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        ans=[]
        rows=len(matrix)
        cols=len(matrix[0])
        for j in range(cols):
            temp=[]
            for i in range(rows):
                temp.append(matrix[i][j])
            ans.append(temp)
        return ans 
        