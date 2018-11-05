m, n = 10, 100

def check(remain, pre):
    # 配置する人がいなくなったら終了
    if remain < 0:
        return 0
    if remain == 0:
        return 1

    count = 0
    for i in range(pre,m+1):
        count += check(remain -i, i)
    return count

print(check(n, 2))
