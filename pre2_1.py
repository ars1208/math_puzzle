def nPr(n, r):
    ans = 1
    for i in range(r,n+1):
        ans *= i
    return ans

print(nPr(5,3))
