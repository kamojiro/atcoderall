N = int( input())
S = []
Sum = 0
for _ in range(N):
    s = int( input())
    Sum += s
    S.append(s)
S.sort()
ans = 0
if Sum%10 == 0:
    for s in S:
        if s%10 != 0:
            ans = Sum - s
            break
else:
    ans = Sum
print(ans)
