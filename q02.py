N = 29

a, b = 1, 17
n = abs(a-b)
# コツはシフト演算子を使用すること
print((1 << (n-1)) + (1 << (N-n-1)) - 1)
