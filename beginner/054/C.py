from itertools import permutations
N, M = map( int, input().split())
edges = [[] for _ in range(N)]
for i in range(M):
    a, b = map( int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
ans = 0
for X in permutations(range(N),N):
    if X[0] != 0:
        continue
    Flag = True
    for i in range(1,N):
        if X[i] in edges[X[i-1]]:
            pass
        else:
            Flag = False
            break
    if Flag:
        ans += 1
print(ans)

