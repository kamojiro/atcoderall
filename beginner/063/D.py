N, A, B = map( int, input().split())
hmax = 0
H = [ int( input()) for _ in range(N)]
hmax = max(H)
L = 0
R = hmax//B + 1
add = A-B
#以下よりも早い
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
    
    
    
    
