N, M, q = map( int, input().split())
X = [0]*M
P = [0]*M
for i in range(M):
    x, p = map( int, input().split())
    X[i] = x
    P[i] = p

while R-L != 1:#L != R:
    now = (L+R)//2
    need = 0
    for i in range(N):
        r = H[i] - now*B
        if r > 0:
            need += (r-1)//add+1
    if need <= now:##うまくいくとき
        R = now
    else:##うまくいかないとき
        L = now#+1 ##うまく行かないので+1している．これがないと無限ループが発生する。
print(R)
