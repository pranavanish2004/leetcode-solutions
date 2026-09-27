from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue=deque()
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
                if grid[r][c]==1:
                    fresh+=1
        if fresh==0:
            return 0
        minutes=0
        while len(queue)>0 and fresh>0:
            size=len(queue)
            for i in range(size):
                r,c=queue.popleft()
                #Down
                if r+1<rows and grid[r+1][c]==1:
                    grid[r+1][c]=2
                    fresh-=1
                    queue.append((r+1,c))
                #up
                if r-1>=0 and grid[r-1][c]==1:
                    grid[r-1][c]=2
                    fresh-=1
                    queue.append((r-1,c))
                #left
                if c-1>=0 and grid[r][c-1]==1:
                    grid[r][c-1]=2
                    fresh-=1
                    queue.append((r,c-1))
                if c+1<cols and grid[r][c+1]==1:
                    grid[r][c+1]=2
                    fresh-=1
                    queue.append((r,c+1))
            minutes+=1
        if fresh>0:
            return -1
        return minutes