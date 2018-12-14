N, X = map( int, input().split())
now = "P"
A = [1]*(N+1)
P = [1]*(N+1)
for i in range(N):
    A[i+1] = 2*A[i]+3
    P[i+1] = 2*P[i]+1
now = N
ans = 0
X -= 1
while now > 0:
    if A[now]//2 == X:
        ans += P[now-1]+1
        X = -1
        break
    elif A[now]//2 < X:
        ans += P[now-1]+1
        X -= A[now-1]+2
    else:
        X -= 1
    if X < 0:
        break
    now -= 1
if X >= 0:
    ans += 1
print(ans)
