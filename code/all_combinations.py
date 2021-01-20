from typing import List


def all_combinations(n: int, k: int) -> List[List[int]]:

    ret_val = list()

    def _all_combinations(i: int, k: int, curr: List[int]):
        if k == 0:
            ret_val.append(curr.copy())
            return

        if i > n:
            return

        # option 1: include the current number and recurse
        curr.append(i)
        _all_combinations(i + 1, k - 1, curr)
        curr.pop()

        # option 2: recurse without the current number
        _all_combinations(i + 1, k, curr)

    _all_combinations(i=1, k=k, curr=list())
    return ret_val


assert all_combinations(n=3, k=2) == [[1, 2], [1, 3], [2, 3]]

assert all_combinations(n=4, k=3) == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
