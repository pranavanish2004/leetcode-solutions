from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        queue=deque()
        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    count+=1
                    queue.append((i,j))
                    grid[i][j]='0'
                while(len(queue)>0):
                    r,c=queue.popleft()
                     # Down
                    if r + 1 < rows and grid[r + 1][c] == "1":
                        grid[r + 1][c] = "0"
                        queue.append((r + 1, c))
                        # Up
                    if r - 1 >= 0 and grid[r - 1][c] == "1":
                        grid[r - 1][c] = "0"
                        queue.append((r - 1, c))

                        # Right
                    if c + 1 < cols and grid[r][c + 1] == "1":
                        grid[r][c + 1] = "0"
                        queue.append((r, c + 1))

                        # Left
                    if c - 1 >= 0 and grid[r][c - 1] == "1":
                        grid[r][c - 1] = "0"
                        queue.append((r, c - 1))

        return count
