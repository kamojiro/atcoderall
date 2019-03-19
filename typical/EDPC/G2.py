def topologicalsort(N,E):
    V = [0]*N
    for i in range(N):
        for y in E[i]:
            V[y] += 1
    S = [ i for i in range(N) if V[i] == 0]
    SORTED = []
    while S:
        s = S.pop(0)
        SORTED.append(s)
        for t in E[s]:
            V[t] -= 1
            if V[t] == 0:
                S.append(t)
    return SORTED
    
N, M = map( int, input().split())
E = [ [] for _ in range(N)]
for _ in range(M):
    x, y = map( int, input().split())
    x, y = x-1, y-1
    E[x].append(y)
V = topologicalsort(N, E)
ANS = [0]*N
for i in range(N):
    v = V[i]
    t = ANS[v]+1
    for e in E[v]:
        if t > ANS[e]:
            ANS[e] = t
print( max(ANS)) 
       
