from copy import deepcopy
N, M = map( int, input().split())
E = dict()
D = dict()
V = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = input().split()
    a, b = int(a)-1, int(b)-1
    V[a].append(b)
    V[b].append(a)
    if c == 'r':
        E[(a,b)] = 1
        E[(b,a)] = 1
    else:
        E[(a,b)] = -1
        E[(b,a)] = -1
    D[(a,b)] = D[(b,a)] = 1

def search(V, D, E, s,c, ans):
    got = [ -1 for _ in range(N)]
    got[s] = 0
    q = [(s,c,0)]
    dD = deepcopy(D)
    while q:
        x, c, d = q.pop()
        c *= -1
        d = (d+1)%2
        for y in V[x]:
            if dD[(x,y)] == 1 and E[(x,y)] == c:
                if got[y] == -1:
                    q.append((y,c))
                    got[y] = d
                else:
                    got
                    
                
        
        
    
for c in [1,-1]:
    for s in range(N):
        


