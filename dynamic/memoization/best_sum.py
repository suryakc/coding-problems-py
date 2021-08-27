""" Return the best combination of numbers (smallest set) from the given array that add up to the given target value. 
Same number can be used multiple times. Only positive integers. """


def best_sum(target, arr):
    """ Get the best subset of numbers that add up to target """
    """ recursion - O(n^m * m) - branching factor is length of the array - n """
    if target == 0:
        return None
    if target in arr:
        return [target]
    
    combination = []

    for num in arr:
        if target < num:
            continue
        new_target = target - num
        if new_target == 0:
            combination.clear()
            combination.append(num)
            break
        else:
            subset = best_sum(new_target, arr)
            if subset is not None:
                curr_len = len(combination)
                candidate_len = len(subset) + 1
                if curr_len == 0 or curr_len > candidate_len:
                    combination.clear()
                    combination.append(num)
                    combination.extend(subset)
    
    if len(combination) == 0:
        return None
    return combination


def best_sum_memo(target, arr, memo = {}):
    """ Get the best subset of numbers that add up to target """
    """ memoization - O(n*m*m) """
    if target == 0:
        return None
    if target in arr:
        return [target]
    if target in memo:
        return memo[target]
    
    combination = []

    for num in arr:
        if target < num:
            continue
        new_target = target - num
        if new_target == 0:
            combination.clear()
            combination.append(num)
            break
        subset = best_sum_memo(new_target, arr, memo)
        if subset is not None:
            curr_len = len(combination)
            candidate_len = len(subset) + 1
            if curr_len == 0 or curr_len > candidate_len:
                combination.clear()
                combination.append(num)
                combination.extend(subset)
    
    if len(combination) == 0:
        return None
    memo[target] = combination
    return combination


def best_sum_memo_better(target, arr, memo = {}):
    """ WIP**** Get the best subset of numbers that add up to target,
        without running out of recursion depth """
    """ memoization - O(n*m*m) """
    if target == 0:
        return None
    if target in arr:
        return [target]
    if target in memo:
        return memo[target]
    
    combination = []

    for num in arr:
        if target < num:
            continue
        subset = []
        new_target = target - num
        if target % num == 0:
            subset = [num] * int(target / num)
        else:
            subset = best_sum_memo_better(new_target, arr, memo)            
    
        if subset is not None:
            curr_len = len(combination)
            candidate_len = len(subset) + 1
            if curr_len == 0 or curr_len > candidate_len:
                combination.clear()
                combination.append(num)
                combination.extend(subset)

    if len(combination) == 0:
        return None
    memo[target] = combination
    return combination


if __name__ == "__main__":
    print(best_sum(100, [2, 5, 3, 13]))