N, M, q = map( int, input().split())
X = [0]*M
P = [0]*M
for i in range(M):
    x, p = map( int, input().split())
    X[i] = x
    P[i] = p
XP = [0]*M
for i in range(M):
    XP[i] = X[i]*P[i]/q
XP.sort()
if M%2 == 1:
    m = XP[M//2]
    exp = 0
    for i in range(M):
        exp += P[i]*abs(X[i]-m)
    print(exp*N)
else:
    m = XP[M//2]
    n = XP[M//2-1]
    expm = 0
    expn = 0
    for i in range(M):
        expm += P[i]*abs(X[i]-m)
        expn += P[i]*abs(X[i]-n)
    exp = min( expn, expm)
    print(exp*N)
