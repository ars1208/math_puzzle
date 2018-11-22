N = 12

cnt = {}
for i in range(1,4000):
    cnt[len(roman(n))] += 1

print(cnt[N])
