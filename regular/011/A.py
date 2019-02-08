m, n, N = map( int, input().split())
now = N
ans = N
while now >= m:
    ans += now//m*n
    now = now%m + now//m*n
print(ans)
