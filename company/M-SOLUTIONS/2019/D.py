from collections import deque
N = int( input())
E = [[] for _ in range(N)]
V = [0]*N
for _ in range(N-1):
    a, b = map( int, input().split())
    a, b = a-1, b-1
    E[a].append(b)
    E[b].append(a)
    V[a] += 1
    V[b] += 1
C = list(map( int, input().split()))
C.sort(reverse=True)
for i in range(N):
    if V[i] == 1:
        s = i
        break
q = deque([s])
V = [0]*N
l = 0
for l in range(N):
    t = q.popleft()
    V[t] = C[l]
    for v in E[t]:
        if V[v] == 0:
            q.append(v)
print( sum(C) - C[0])
print( " ".join( map( str, C)))
