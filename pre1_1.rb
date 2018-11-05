#最大の人数Mと分ける人数N
M, N = 6,6

def check(remain, pre) #remain:残った人数 pre:前のテーブルに配置した人数
    #配置する人がいなくなると終了
    return 0 if remain < 0
    return 1 if remain == 0

    cnt = 0
    pre.upto(M) do |i|
        cnt += check(remain - i, i)
    end
    cnt
end

puts check(N, 2)
