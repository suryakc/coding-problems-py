""" Given a target string and an array of strings, return the number of ways 
    the target string can be constructed using the strings. 
    
    arr: ["ab", "abc", "cd", "def", "abcd"]
    target: "abcdef"
    result: 1

    arr: ["bo", "rd", "ate", "ska", "sk", "boar"]
    target: "skateboard"
    result: 0

    """


def count_construct(target, arr):
    if not target:
        return 1
    counter = 0

    for str in arr:
        if str == target:
            counter += 1
            continue
        if target.startswith(str):
            subTarget = target[len(str):]
            subResult = count_construct(subTarget, arr)
            if subResult == 0:
                continue
            counter += subResult
    
    return counter


def count_construct_memo(target, arr, memo = {}):
    if not target:
        return 1
    if target in memo:
        return memo[target]
    counter = 0

    for str in arr:
        if target.startswith(str):
            subTarget = target[len(str):]
            subResult = count_construct_memo(subTarget, arr, memo)
            if subResult == 0:
                continue
            counter += subResult
    
    memo[target] = counter
    return counter


if __name__ == "__main__":
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(count_construct("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
    print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(count_construct_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "df"]))
