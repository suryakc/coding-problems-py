""" Given a target string and an array of strings, determine if the target string
    can be constructed using the strings. 
    
    arr: ["ab", "abc", "cd", "def", "abcd"]
    target: "abcdef"
    result: True

    arr: ["bo", "rd", "ate", "ska", "sk", "boar"]
    target: "skateboard"
    result: False

    """


def can_construct(target, arr):
    if target is None:
        return True
    if target in arr:
        return True

    for str in arr:
        index = target.find(str)
        """ print(f"{str} is in {target} at {index}") """
        if index > -1:
            subTargetLeft = target[:index]
            subResultLeft = not subTargetLeft or can_construct(subTargetLeft, arr)
            if not subResultLeft:
                continue
            subTargetRight = target[index+len(str):]
            subResultRight = not subTargetRight or can_construct(subTargetRight, arr)
            if subResultLeft and subResultRight:
                return True
    
    return False


def can_construct_memo(target, arr, memo = {}):
    if not target:
        return True
    if target in arr:
        return True
    if target in memo:
        return memo[target]

    for str in arr:
        index = target.find(str)
        """ print(f"{str} is in {target} at {index}") """
        if index > -1:
            subTargetLeft = target[:index]
            subResultLeft = not subTargetLeft or can_construct_memo(subTargetLeft, arr)
            if not subResultLeft:
                continue
            subTargetRight = target[index+len(str):]
            subResultRight = not subTargetRight or can_construct_memo(subTargetRight, arr)
            if subResultLeft and subResultRight:
                memo[target] = True
                return True
    
    memo[target] = False
    return False


if __name__ == "__main__":
    print(can_construct("bcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(can_construct("skateboard", ["bo", "rd", "ate", "ska", "sk", "boar"]))
    print(can_construct_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
