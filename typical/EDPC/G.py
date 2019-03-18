N, M = map( int, input().split())
V = [ 1 for i in range(N)]
E = [ [] for _ in range(N)]
for _ in range(M):
    x, y = map( lambda x:x-1, map( int, input().split()))
    V[y] = 0
    E[x].append(y)
S = []
for i in range(N):
    if V[i] == 1:
        S.append(i)
Pathdistance = [-1 for _ in range(N)]
while S:
    s = S.pop(0)
    Pathdistance[s] = 0
    now = 1
    Z = []
    for t in E[s]:
        if Pathdistance[t] < now:
            Z.append(t)
            Pathdistance[t] = now
    while Z:
        T = []
        now += 1
        for z in Z:
            for t in E[z]:
                if Pathdistance[t] < now:
                    T.append(t)
                    Pathdistance[t] = now
        Z = T
print( max(Pathdistance))
                
