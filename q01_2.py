N = 100

cnt = 0
for l in range(N+1):
    for r in range(l,N+1):
        all = [l, r-l, N-r]
        max_index = [i for i, x in enumerate(all) if x == max(all)]
        if len(max_index) == 1:
            cnt += 1

print(cnt)
