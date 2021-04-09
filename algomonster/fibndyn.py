import time

N = 10000


def fibn(n, memo):
    if n <= 2:
        return 1 
    if n in memo:
        return memo[n]
    else:
        f = fibn(n - 1, memo) + fibn(n - 2, memo)
        memo[n] = f
        return f

def btmupfib(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    prev_2 = 0
    prev_1 = 1
    for i in range(2, n + 1):
        f = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = f
    return f

start = time.time()
print(btmupfib(N))
end = time.time()
print(end - start)
