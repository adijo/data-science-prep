from typing import List


def max_sum_increasing_subsequence(arr: List[int]) -> int:
    dp = arr.copy()
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], arr[i] + dp[j])
    return max(dp)


assert max_sum_increasing_subsequence([5, 4, 3, 2, 1]) == 5
assert max_sum_increasing_subsequence([3, 2, 5, 7, 6]) == 15
