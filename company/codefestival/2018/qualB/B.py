N, X = map( int, input().split())
C = [[]]*N
D = [[]]*N
for i in range(N):
    a, b = map( int, input().split())
    D[i] = [b,a]
D = sorted(D)
z, w = D[-1]
ans = z*(w+X)
for i in range(N-1):
    a, b = D[i]
    ans += a*b
print(ans)
