pointperquery=2312311
ans = 0
for _ in range(1000):
    ans += pointperquery
    pointperquery *= 0.998
print(round(ans))
