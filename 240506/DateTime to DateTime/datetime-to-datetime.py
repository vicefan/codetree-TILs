d, t, m = map(int, input().split())
min_calc = (d - 11) * 24 * 60 + (t - 11) * 60 + m - 11

print(min_calc) if min_calc > 0 else print(-1)