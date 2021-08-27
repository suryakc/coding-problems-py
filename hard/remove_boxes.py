""" Given a list of positive numbers, remove numbers from the list
    until the list is empty. In each attempt to remove, you 
    will get k*k points for k consecutive occurences of a 
    single number. You may remove only 1 or more occurences 
    of the same number in a single attempt. Return the maximum 
    points you can score.
    
    Example: [2, 2, 2]
    Result: 9 (3*3)
    
    Example: [1, 1, 3, 1, 4, 5, 4, 4, 4]
    Result: 27
     """


from collections import OrderedDict


def remove_numbers(nums):
    if len(nums) <= 1:
        return len(nums)
    
    map = OrderedDict()
    previous_num = nums[0]
    start_index = 0
    for index, value in enumerate(nums):
        if previous_num != value:
            start_index = index
        key = str(value) + str(start_index)        
        if value not in map:
            map[key] = 1
        else:
            map[key] += 1

    print(map)
    result = sum([v*v for k,v in sorted(map.items(), key=lambda item: item[1])])
    return result


if __name__ == "__main__":
    print(remove_numbers([2, 2, 2]))
    print(remove_numbers([1, 1, 3, 1, 4, 5, 4, 4, 4]))
    print(remove_numbers([1,3,2,2,2,3,4,3,1]))
