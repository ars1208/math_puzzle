N = 4

cnt = 0
for rock in range(N+1):
    for scissors in range(N+1 - rock):
        paper = N - rock - scissors
        all = [rock, scissors, paper]
        max_index = [i for i, x in enumerate(all) if x == max(all)]
        if len(max_index) == 1:
            cnt += 1

print(cnt)
