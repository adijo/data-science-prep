from typing import List


def intersection_time_optimized(a: List[int], b: List[int]) -> List[int]:
    """
    O(n) space, O(n) time
    """
    return list(set(a) & set(b))


def intersection_space_optimized(a: List[int], b: List[int]) -> List[int]:
    """
    O(1) auxiliary space (apart from storing the result), O(n log n) time
    """
    a.sort()
    b.sort()
    i, j = 0, 0
    ret_val = list()
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            ret_val.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return ret_val


assert intersection_space_optimized([2, 4, 1, 5, 0], [3, 4, 5]) == [4, 5]
