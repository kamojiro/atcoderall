from collections import defaultdict, deque
N = int( input())
d = defaultdict( int)
E = [ [] for _ in range(N)]
for _ in range(N-1):
    u, v, w = map( int, input().split())
    u = u-1
    v = v-1
    E[u].append(v)
    E[v].append(u)
    d[(u,v)] = w%2
    d[(v,u)] = w%2
V = [-1]*N
V[0] = 0
q = deque([0])
while q:
    v = q.popleft()
    l = V[v]
    for t in E[v]:
        if V[t] == -1:
            V[t] = (l+d[(v,t)])%2
            q.append(t)
for i in range(N):
    print(V[i])
