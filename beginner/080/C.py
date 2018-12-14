from itertools import product
N = int(input())
F = [ list( map( int, input().split())) for _ in range(N)]
P = [ list( map( int, input().split())) for _ in range(N)]
ans = - 10**10
for X in product( range(2), repeat = 10):
    if X == tuple([0]*10):
        pass
    else:
        c = 0
        for i in range(N):
            n = 0
            for j in range(10):
                if F[i][j] == 1 and X[j] == 1:
                    n += 1
            c += P[i][n]
        ans = max(ans, c)
print(ans)
                
        
        
