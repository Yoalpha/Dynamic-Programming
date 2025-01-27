#classic fib function
def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(6))
print(fib(7))
print(fib(8))

#classic fib recursion algorithm times out because it takes too much time to run
#print(fib(50))


#memoization
#key -> args
#value -> return value
memo = {}
def fib2(n):
    #base case to return n branch sum if n is already computed
    if n in memo:
        return memo[n]

    #base case that returns 1 once the branch bottoms out
    if n <= 2:
        return 1

    #storing the new compute and returning the newly computed value
    memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]

print(fib2(50))

