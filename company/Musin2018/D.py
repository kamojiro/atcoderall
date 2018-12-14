from itertools import product
N, M = map( int, input().split())
ans = 0
for K in product(range(1,N+1),range(1,M+1)):
    x, y = K[0], K[1]
    x,y = min(x,y),max(x,y)
    revx = int(str(x)[::-1])
    if revx+y == x or :
        ans += 1
print(ans)

