#write a function that takes in a target sum and an array of numbers as arguments
#the function returns a boolean indication if the sum can be generated using the numbers in the array
#you can use an element of the array as many times as needed
#you may assume that all input numbers are non-negative

# classic approach
def canSum(target, nums):
    if target == 0:
        return True

    if target < 0:
        return False

    for num in nums:
        rem = target - num

        if canSum(rem, nums) == True:
            return True

    return False

print(canSum(7, [2, 3]))
print(canSum(7, [5, 3, 4, 7]))

# Memoization
memo = {}
def canSumMemo(target, nums):
    if target in memo:
        return memo[target]

    if target == 0:
        return True

    if target < 0:
        return False


    for num in nums:
        rem = target - num

        if canSumMemo(rem, nums) == True:
            memo[target] = True
            return True
    memo[target] = False
    return False

print(canSumMemo(300, [7, 14]))


