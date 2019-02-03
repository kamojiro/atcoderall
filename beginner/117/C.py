N, M = map( int, input().split())
X = list( map( int, input().split()))
X.sort()
XS = [0]*(M-1)

if N >= M:
    print(0)
else:
    for i in range(M-1):
        XS[i] = X[i+1] - X[i]
    XS.sort( key = None, reverse = True)
    ans = X[-1] - X[0]
    ans -= sum( XS[:N-1])
    print(ans)
