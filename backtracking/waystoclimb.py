# I can climb 1,2 or 3 steps at a time.
# in how many ways I can climb a n-stepped ladder?


# n = 3, result = 3 [1,1,1] [1,2] [2,1]
# n = 4, result = 7 [1,1,1,1] [1,1,2] [1,2,1] [2,1,1] [1,3] [3,1] [2,2]

def solution(n):
    memo = {}
    def dfs(steps, res):
        if steps == 0:
            return 1
        else:
            ways = 0
            for i in range(1,4):
                if steps - i < 0:
                    continue
                if steps - i in memo:
                    ways += memo[steps - i]
                else:
                    ways += res + dfs(steps - i, res)
                    memo[steps - i] = ways
            return ways
    return dfs(n, 0)

print(solution(500))
            
