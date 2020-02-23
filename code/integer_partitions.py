from typing import List

from common import reverse


def generate_integer_partitions(target: int) -> List[List[int]]:

    ret_val = list()

    def _generate(n: int, max_val: int, curr_partition: List[int]) -> None:
        if n == 0:
            ret_val.append(reverse(curr_partition.copy()))
        else:
            if max_val <= n:
                curr_partition.append(max_val)
                _generate(n - max_val, max_val, curr_partition)
                curr_partition.pop()

            if max_val > 1:
                _generate(n, max_val - 1, curr_partition)

    _generate(target, target, list())
    return reverse(ret_val)


assert generate_integer_partitions(4) == [
    [1, 1, 1, 1],
    [1, 1, 2],
    [2, 2],
    [1, 3],
    [4]
]

assert generate_integer_partitions(5) == [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 2],
    [1, 2, 2],
    [1, 1, 3],
    [2, 3],
    [1, 4],
    [5]
]
