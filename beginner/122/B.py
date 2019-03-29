S = input()
ans = 0
now = 0
for s in S:
    if s == 'A' or s == 'C' or s == 'G' or s == 'T':
        now += 1
    else:
        if ans < now:
            ans = now
        now = 0
if ans < now:
    ans = now
print(ans)
