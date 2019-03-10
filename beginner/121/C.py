N, M = map( int, input().split())
A = [ list( map( int, input().split())) for _ in range(N)]
A.sort()
ans = 0
now = 0
for i in range(N):
    if now + A[i][1] <= M:
        ans += A[i][0]*A[i][1]
        now += A[i][1]
    else:
        ans += A[i][0]*(M - now)
        break
print( ans)
