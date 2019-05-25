N = int( input())
ans = 0
for _ in range(N):
    a, b = map( int, input().split())
    if a >= b:
        ans += a
    else:
        ans += b

print(ans)
