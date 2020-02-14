m, n = 10, 100

memo = dict()
def check(x, t):
    if (x, t) in memo:
        return memo[(x,t)]
    if x == 0:
        return 1
    if x < 0:
        return 0

    cnt = 0
    for i in range(t,m+1):
        cnt += check(x-i,i)
    memo[(x,t)] = cnt

    return cnt

print(check(n,2))
