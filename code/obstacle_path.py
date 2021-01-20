from typing import List


def obstacle_paths(grid: List[List[int]]) -> int:

    obstacle = 1
    m, n = len(grid), len(grid[0])

    # dp[i][j] contains the value for the number of paths from
    # i, j to the final destination len(grid) - 1, len(grid[0]) - 1

    dp = [[0 for _ in range(n)] for _ in range(m)]

    def _is_valid(i: int, j: int) -> bool:
        return 0 <= i < m and 0 <= j < n

    dest_i, dest_j = m - 1, n - 1

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):

            if grid[i][j] == obstacle:
                continue

            # base case
            if i == dest_i and j == dest_j:
                dp[i][j] = 1

            if _is_valid(i + 1, j):
                dp[i][j] += dp[i + 1][j]

            if _is_valid(i, j + 1):
                dp[i][j] += dp[i][j + 1]

    return dp[0][0]


assert obstacle_paths([[0, 0, 0], [1, 1, 0], [0, 1, 0]]) == 1

assert obstacle_paths([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2

assert obstacle_paths([[0, 0]]) == 1
