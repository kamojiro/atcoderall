N, L = map( int, input().split())
now = abs(L)
for i in range(N):
    if abs(L+i) < now:
        now = abs(L+i)
ans = 0
for i in range(N):
    if abs(L+i) == now:
        continue
    ans += L+i
print(ans)
