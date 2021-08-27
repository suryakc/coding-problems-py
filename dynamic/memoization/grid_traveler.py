""" Solve the 2d grid traveler problem.
    Given a m*n grid, return the number of ways
    the grid can be traversed. """


from functools import lru_cache


def grid_traveler(m, n):
    """ Recursive implementation """
    if m == 0 or n == 0:
        return 0
    if m == 1 and n ==1:
        return 1
    
    return grid_traveler(m-1, n) + grid_traveler(m, n-1)


def grid_traveler_memo(m, n, memo = { "1,1": 1 }):
    """ Memoization """
    key = "%d,%d"%(m,n)
    if key in memo:
        return memo[key]        
    if m == 0 or n == 0:
        memo[key] = 0
        return 0
    
    left = grid_traveler_memo(m-1, n, memo)
    memo["%d,%d"%(m-1,n)] = left
    right = grid_traveler_memo(m, n-1, memo)
    memo["%d,%d"%(m,n-1)] = right
    return left + right


@lru_cache
def grid_traveler_lru_cache(m, n):
    """ built in tools """
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    
    return grid_traveler_lru_cache(m-1, n) + grid_traveler_lru_cache(m, n-1)


if __name__ == "__main__":
    print(grid_traveler(2, 3))
    print(grid_traveler_memo(20, 20))
    print(grid_traveler_lru_cache(20, 20))
