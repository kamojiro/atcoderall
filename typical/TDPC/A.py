from copy import deepcopy
N = int( input())
P = list( map(int, input().split()))
Q = set([0])
for i in range(N):
    R = deepcopy(Q)
    p = P[i]
    for r in R:
        Q.add(r+p)
print(len(Q))
        
    
