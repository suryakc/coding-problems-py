""" Given a target string and an array of strings, return the all the ways 
    the target string can be constructed using the strings. 
    
    arr: ["ab", "abc", "cd", "def", "abcd"]
    target: "abcdef"
    result: [["abc", "def"]]

    arr: ["bo", "rd", "ate", "ska", "sk", "boar"]
    target: "skateboard"
    result: []

    """


def all_construct(target, arr):
    if not target:
        return 1
    combinations = []

    for str in arr:
        if str == target:
            combinations.append([str])
            continue
        if target.startswith(str):
            subTarget = target[len(str):]
            subResult = all_construct(subTarget, arr)
            if len(subResult) == 0:
                continue
            combinations.extend([str] + x for x in subResult)
    
    return combinations


def all_construct_memo(target, arr, memo = {}):
    if not target:
        return 1
    if target in memo:
        return memo[target]
    combinations = []

    for str in arr:
        if str == target:
            combinations.append([str])
            continue
        if target.startswith(str):
            subTarget = target[len(str):]
            subResult = all_construct_memo(subTarget, arr, memo)
            if len(subResult) == 0:
                continue
            combinations.extend([str] + x for x in subResult)
    
    memo[target] = combinations
    return combinations


if __name__ == "__main__":
    print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(all_construct("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
    print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(all_construct_memo("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(all_construct_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "df"]))
