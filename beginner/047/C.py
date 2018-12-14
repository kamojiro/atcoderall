S = input()
now = S[0]
ans = 0
for s in S[1:]:
    if not s == now:
        now = s
        ans += 1
print(ans)
