N, T = map( int, input().split())
A = [ int( input()) for _ in range(N)]
ans = T
now = A[0]
for i in range(1,N):
    if now + T <= A[i]:
        ans += T
    else:
        ans += A[i] - now
    now = A[i]
print( ans)
