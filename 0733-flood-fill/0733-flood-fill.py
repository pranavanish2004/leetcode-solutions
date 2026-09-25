from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        old = image[sr][sc]

        # If the new color is already the same
        if old == color:
            return image

        rows = len(image)
        cols = len(image[0])

        queue = deque()

        # Start BFS from starting cell
        queue.append((sr, sc))

        # Change color immediately
        image[sr][sc] = color

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while len(queue) > 0:

            r, c = queue.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Check if valid cell and has old color
                if (0 <= nr < rows and
                    0 <= nc < cols and
                    image[nr][nc] == old):

                    image[nr][nc] = color
                    queue.append((nr, nc))

        return image