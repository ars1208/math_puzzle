memo = [1]

def factorial(n):
    if len(memo) == n:
        return memo[n]
    print(memo)
    memo.append(n * factorial(n-1))

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

print(nCr(5,3))
