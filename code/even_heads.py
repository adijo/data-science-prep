from functools import lru_cache
from common import almost_equal


def even_heads(tosses: int, p: float) -> float:

    @lru_cache(maxsize=128)
    def _even_heads(n: int, even: bool) -> float:
        if n == 0:
            return 1 if even else 0
        else:
            return p * _even_heads(n - 1, not even) + (1 - p) * _even_heads(n - 1, even)

    return _even_heads(tosses, even=True)


assert even_heads(10, p=0.5) == 0.5
assert almost_equal(even_heads(10, p=0.6), 0.5000000512)
