""" Given an array of integers, write a function to return an 
    array such that at each index, it contains the product of 
    all numbers in the source array except the number at the 
    index.
    Example:
    input: [3, 5, 2, 4]
    result: [40, 24, 60, 30] """


def product_except_itself(nums):
    size = len(nums)
    if size <= 1:
        return nums
    
    result = [1]
    for i in range(1, size):
        result.append(result[i-1] * nums[i-1])

    temp = 1
    for i in range(size-2, -1, -1):
        print(i)
        temp = nums[i+1] * temp
        result[i] = result[i] * temp
        
    return result


if __name__ == "__main__":
    print(product_except_itself([3, 5, 2, 4]))
        
