from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        queue=deque()
        row=len(mat)
        cols=len(mat[0])
        queue=deque()
        for i in range(row):
            for j in range(cols):
                if mat[i][j]==0:
                    queue.append((i,j))
                else:
                    mat[i][j]=-1
        while(len(queue)>0):
            i,j=queue.popleft()
            if(i+1<row and mat[i+1][j]==-1):
                mat[i+1][j]=mat[i][j]+1
                queue.append((i+1,j))
            if(i-1>=0 and mat[i-1][j]==-1):
                mat[i-1][j]=mat[i][j]+1
                queue.append((i-1,j))
            if(j+1<cols and mat[i][j+1]==-1):
                mat[i][j+1]=mat[i][j]+1
                queue.append((i,j+1))
            if(j-1>=0 and mat[i][j-1]==-1):
                mat[i][j-1]=mat[i][j]+1
                queue.append((i,j-1))
        return mat
            

                
        



        