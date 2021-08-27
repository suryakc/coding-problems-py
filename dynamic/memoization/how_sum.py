""" Return the combination of numbers from the given array that add up to the given target value. 
Same number can be used multiple times. Only positive integers. """

def how_sum(target, arr):
    """ Get the subset of numbers that add up to target"""
    """ recursion - O(n^m * m) - branching factor is length of the array - n """
    if target <= 0:
        return None
    if target in arr:
        return [target]

    combination = []
    
    for num in arr:
        if target < num:
            continue
        new_target = target - num
        if new_target == 0:
            combination.append(num)
            break
        subset = how_sum(new_target, arr)
        if subset is not None:
            combination.append(num)
            combination.extend(subset)
            break
    
    if len(combination) == 0:
        return None
    return combination


def how_sum_lru_cache(target, arr):
    """ Get the subset of numbers that add up to target"""
    """ recursion - O(n*m*m) """
    if target <= 0:
        return None
    if target in arr:
        return [target]
    
    combination = []
    for num in arr:
        if target < num:
            continue
        new_target = target - num
        if new_target == 0:
            combination.append(num)
            break
        subset = how_sum_lru_cache(new_target, arr)
        if subset is not None:
            combination.append(num)
            combination.extend(subset)

    if len(combination) == 0:
        return None
    return combination


if __name__ == "__main__":
    print(how_sum_lru_cache(9201, [2, 4, 1]))