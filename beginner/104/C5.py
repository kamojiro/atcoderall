from itertools import product
D, G = map( int, input().split())
P = []
C = []
SUM = []
for i in range(D):
    p, c = map( int, input().split())
    P.append(p)
    SUM.append(p*100*(i+1) + c)

ans = 1000
for X in product(range(2), repeat = D):
    cnt = 0
    com = 0
    K = []
    for i in range(D):
        if X[i] == 1:
            cnt += P[i]
            com += SUM[i]
        else:
            K.append(i)
    if com >= G:
        ans = min(ans, cnt)
    else:
        for k in K:
            need = min((G-com-1)//(100*(k+1))+1,P[k]-1)
            kcnt = cnt + need
            kcom = com + need*100*(k+1)
            if kcom >= G:
                ans = min(ans,kcnt)
print(ans)
    
