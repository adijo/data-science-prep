from typing import List


def permutations(nums: List[int]) -> List[List[int]]:
    ret_val: List[List[int]] = list()

    def _permutations(curr_nums: List[int], taken: List[bool]):

        if all(taken):
            ret_val.append(curr_nums.copy())
            
        else:
            for idx, num in enumerate(nums):
                if not taken[idx]:
                    taken[idx] = True
                    curr_nums.append(num)
                    _permutations(curr_nums, taken)
                    curr_nums.pop()
                    taken[idx] = False

    _permutations(curr_nums=list(), taken=[False for _ in range(len(nums))])
    return ret_val


assert permutations([1, 2]) == [[1, 2], [2, 1]]

assert permutations([1, 2, 3]) == [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1],
]
