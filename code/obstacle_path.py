from typing import List


def obstacle_paths(grid: List[List[int]]) -> int:

    obstacle = 1

    # dp[i][j] contains the value for the number of paths from
    # i, j to the final destination len(grid) - 1, len(grid[0]) - 1

    dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    def _is_valid(i: int, j: int) -> bool:
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])

    dest_i, dest_j = len(grid) - 1, len(grid[0]) - 1

    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[0]) - 1, -1, -1):

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
