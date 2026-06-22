class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'

            while q:
                row, col = q.popleft()
                for r, c in directions:
                    nr, nc = row + r, col + c
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1':
                        q.append((nr, nc))
                        grid[nr][nc] = '0'
                    



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1

        return islands