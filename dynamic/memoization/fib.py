""" Generating fibonacci numbers """
from functools import lru_cache


def fib_rec(n):
    """ Generate nth fibonacci number """
    if n <= 2:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)


def fib(n, memo = { 0: 0, 1: 1, 2: 1 }):
    """ Memoization """
    if n in memo:
        return memo[n]
    prev = fib(n-1)
    memo[n-1] = prev
    prev_to_prev = fib(n-2)
    memo[n-2] = prev_to_prev
    return prev + prev_to_prev


@lru_cache
def fib_lru_cache(n):
    """ pyton tools """
    if n in { 0, 1 }:
        return n
    return fib_lru_cache(n-1) + fib_lru_cache(n-2)


if __name__ == "__main__":
    print(fib(48))
    print(fib(49))
    print(fib(50))
    print(fib(300))
    print(fib_lru_cache(300))