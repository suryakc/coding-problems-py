""" Can we generate the given value by summing up a subset of the array elements? 
Same number can be used multiple times. Only positive integers. """


def can_sum(target, arr):
    if target in arr or target == 0:
        return True
    if target < 0:
        return False
    
    for element in arr:
        if target < element:
            continue
        new_target = target % element
        result = (new_target == 0) or can_sum(new_target, arr)
        if result:
            return True
    return False


def can_sum_memo(target, arr, memo = { }):
    if target in arr:
        return True
    if target < 0:
        return False
    if target in memo:
        return memo[target]
    
    for element in arr:
        if target < element:
            continue
        new_target = target % element
        if new_target == 0:
            memo[target] = True
            return True
        if new_target in memo:
            return memo[new_target]
        result = can_sum_memo(new_target, arr, memo)
        memo[new_target] = result
        if result:            
            return True

    memo[target] = False
    return False


if __name__ == "__main__":
    print(can_sum(4, [5, 3, 4]))
    print(can_sum(2, [5, 3, 4]))
    print(can_sum_memo(9201, [7, 2, 14, 1, 22, 21, 10, 11, 41]))
