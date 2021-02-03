def palindromic_subset(n: int) -> int:

    dp = dict()
    s = str(n)

    def _palindromic_subset(i: int, j: int) -> int:
        if i > j:
            return 0
        elif i == j:
            return 1
        elif (i, j) in dp:
            return dp[(i, j)]
        else:
            ret_val = max(_palindromic_subset(i + 1, j), _palindromic_subset(i, j - 1))

            if s[i] == s[j]:
                ret_val = max(ret_val, 2 + _palindromic_subset(i + 1, j - 1))

            dp[(i, j)] = ret_val

            return dp[(i, j)]

    return _palindromic_subset(0, len(s) - 1)


assert palindromic_subset(93567619) == 5
assert palindromic_subset(22242) == 4
assert palindromic_subset(1223) == 2
