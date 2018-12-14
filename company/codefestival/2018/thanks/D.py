S = input()
ans = 1
now = S[0]
for s in S[1:]:
    if now >= s:
        ans += 1
        now = s
print(ans)
