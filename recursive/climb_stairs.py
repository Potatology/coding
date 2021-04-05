
def climbStairs(n):
    return helper_climb(0, n)

def helper_climb(i, n):
    if i > n:
        return 0
    elif i == n:
        return 1
    return helper_climb(i + 1, n) + helper_climb(i + 2, n)
        
print(climbStairs(30))
        