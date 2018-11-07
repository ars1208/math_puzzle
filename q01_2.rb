N = 100

cnt = 0
0.upto(N) do |l|
    l.upto(N) do |r|
        all = [l, r-l, N-r]
        cnt += 1 if all.count(all.max) == 1
    end
end

puts cnt
