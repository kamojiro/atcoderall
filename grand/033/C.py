def diameter(N, E):#diamete of a tree
    from collections import deque
    V = [-1]*N
    V[0] = 0
    q = deque([0])
    while q:
        v = q.popleft()
        for w in E[v]:
            if V[w] == -1:
                V[w] = V[v] + 1
                q.append(w)
    s = V.index( max(V))
    p = deque([s])
    W = [-1]*N
    W[s] = 0
    while p:
        v = p.popleft()
        for w in E[v]:
            if W[w] == -1:
                W[w] = W[v] + 1
                p.append(w)
    return max(W)

N = int( input())
E = [ [] for _ in range(N)]
for _ in range(N-1):
    a, b = map( int, input().split())
    a, b = a-1, b-1
    E[a].append(b)
    E[b].append(a)
ans = "First"
if diameter(N, E)%3 == 1:
    ans = "Second"
print( ans)
