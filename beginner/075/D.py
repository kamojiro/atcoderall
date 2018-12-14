N, K = map( int, input().split())
X = [0]*N
Y = [0]*N
for i in range(N):
    x, y = map( int, input().split())
    X[i] = x
    Y[i] = y
SX = sorted(X)
SY = sorted(Y)
ans = 10**19
for xleft in range(N-1):
    a = SX[ xleft]
    for xright in range(xleft, N):
        b = SX[ xright]
        for yunder in range(N-1):
            c = SY[ yunder]
            for yabove in range(yunder, N):
                d = SY[ yabove]
                cnt = 0
                for i in range(N):
                    if a <= X[i] and X[i] <= b and c <= Y[i] and Y[i] <= d:
                        cnt += 1
                if cnt >= K:
                    ans = min( ans, (b-a)*(d-c))
print(ans)
