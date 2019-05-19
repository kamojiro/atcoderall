from collections import deque
N = int( input())
P = [0]*N
H = [0]*N
E = [ [] for _ in range(N)]
for i in range(1,N):
    p, h = map( int, input().split())
    P[p] = i
    E[i].append(p)
    H[i] = h
d = deque()
V = [ deque() for _ in range(N)]
for i in range(N):
    if not E[i] == 0:
        d.append(i)
while d:
    v = d.popleft()
    for c in E[v]:
        d.append(c)
    if not E[v]:
        continue
    h = H[v]
    V[v] = deque()
    for t in V(E[v][0]):
        if t >= h:
            V[v].append(h)
            h = 10**10
        V[v].append(t)
    if h != 10**10:
        V[v].append(t)
    for w in E[v][1:]:
        h = H[w]
        q = deque()
        for t in V(E[v][w]):
            if t >= h:
                q.append(h)
                h = 10**10
            q.append(t)
        p = deque([10**10]*(len(q)+len(V[v])))
        for 
