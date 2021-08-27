""" Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order. 
    
    Input: [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

    Input: [0]
    Output: [[],[0]]

    Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    """
import itertools


def get_subsets(input_list):
    result = [input_list]
    input_list.sort()
    for i in range(len(input_list)):
        subsets = [list(ele) for ele in list(itertools.combinations(input_list, i))]
        unique_subsets = [list(x) for x in set(tuple(x) for x in subsets)]
        result.extend(unique_subsets)
    return result


if __name__ == "__main__":
    print(get_subsets([4, 4, 4, 1, 4]))
    print(get_subsets([1, 4, 4, 4, 4]))