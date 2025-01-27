# say that you are a traveler on a 2D grid. You begin in the top-left corner and your goal
# is to travel to the bottom-right corner. You may only move down or right.
# in how many ways can you travel to the goal on a grid with dimensions m * n?

#classical approach
def gridTraveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return gridTraveler(m - 1, n) + gridTraveler(m, n-1)


print(gridTraveler(1, 1))
print(gridTraveler(3, 2))
print(gridTraveler(2, 3))

#memoization

memo={}
def gridTraveler2(m, n):
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = gridTraveler2(m - 1, n) + gridTraveler2(m, n-1)
    return memo[key]

print(gridTraveler2(18, 18))
