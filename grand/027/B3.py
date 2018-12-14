from itertools import accumulate

def E(i, x):
    if i == 1:
        return 5*x
    return (2*i+1)*x

N, X = map( int, input().split())
G = list( map( int, input().split()))
G.sort(key=None, reverse = True)
accG = list(accumulate(G))
accG.insert(0,0)
ans = X*2*N + G[0]*N*5
for k in range(1,N+1):
    now = 0
    for i in range(1,N+1):
        if i*k <= N:
            now += E(i, accG[i*k] - accG[(i-1)*k])
        else:
            now += E(i, accG[-1] - accG[(i-1)*k])
            break
    ans = min( ans, now+(N+k)*X)
print(ans)
        
    
    
