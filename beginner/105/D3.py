N, M = map( int, input().split())
A = list( map( int, input().split()))
D = {0:1}
a = 0
ans = 0
for i in range(N):
    a = (a+A[i])%M
    ans += D.get(a,0)
    D[a] = 1 + D.get(a,0)
print(ans)
