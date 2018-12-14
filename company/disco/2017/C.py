N, C = map( int, input().split())
L = [ int( input()) for _ in range(N)]
L.sort()
f = 0
h = N-1
ans = 0
while h-f >= 0:
    if L[f] + L[h] + 1<= C:
        ans += 1
        f += 1
        h -= 1
    else:
        ans += 1
        h -= 1
print(ans)
