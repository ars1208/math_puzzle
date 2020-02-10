m, n = 10, 100

def check(x, t): # 再帰的処理を行なうために関数化。xが残っている人数で、tが前のテーブルの人数

    if x == 0:
        return 1
    elif x < 0:
        return 0

    cnt = 0
    for i in range(t,m+1): # テーブルに座る人数を求める
        cnt += check(x-i, i)
    return cnt

print(check(n,2))
