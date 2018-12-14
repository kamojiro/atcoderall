from collections import defaultdict
N, M = map( int, input().split())
E = [ [] for _ in range(N)]
V = [ 0 for _ in range(N)]
for i in range(M):
    L, R, D = map( int, input().split())
    E[L-1].append((R-1,D))
    V[R-1] += 1
dist = [-1]*N
for i in range(N):
    if V[i]:
        continue
    S = [i]
    dist[i] = 0
    while S:
        v = S.pop()
        for u, d in E[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + d
                S.append(u)
ans = "Yes"
for v in range(N):
    for u, d in E[v]:
        if dist[v] + d != dist[u]:
            ans = "No"
            break
    if ans == "No":
        break
print(ans)
