class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7

        m = len(grid)
        n = len(grid[0])

        # right[i][j]: ways that reach (i, j) moving right
        # down[i][j]: ways that reach (i, j) moving down
        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        # The robot starts at (0, 0). It can initially move right or down.
        if n > 1:
            right[0][1] = 1
        if m > 1:
            down[1][0] = 1

        for i in range(m):
            for j in range(n):
                # The start cell's first moves were handled above.
                if i == 0 and j == 0:
                    continue

                from_left = right[i][j]
                from_above = down[i][j]

                if grid[i][j] == 1:
                    # A path entering this mirror while moving right
                    # is redirected to the cell below it.
                    if i + 1 < m:
                        down[i + 1][j] = (down[i + 1][j] + from_left) % MOD

                    # A path entering this mirror while moving down
                    # is redirected to the cell to its right.
                    if j + 1 < n:
                        right[i][j + 1] = (right[i][j + 1] + from_above) % MOD

                else:
                    # On an empty cell, every path may choose right or down.
                    ways = (from_left + from_above) % MOD

                    if j + 1 < n:
                        right[i][j + 1] = (right[i][j + 1] + ways) % MOD

                    if i + 1 < m:
                        down[i + 1][j] = (down[i + 1][j] + ways) % MOD

        return (right[m - 1][n - 1] + down[m - 1][n - 1]) % MOD
