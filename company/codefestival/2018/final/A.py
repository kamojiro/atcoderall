N, M = map( int, input().split())
R = [[] for _ in range(541)]
for i in range(M):
    a, b, l = map( int, input().split())
    if l <= 1540:
        R[l-1000].append((a,b))
ans = 0

for i in range(270):
    V = [0]*(N+1)
    for a, b in R[i]:
        V[a] += 1
        V[b] += 1
    for c, d in R[540 - i]:
        ans += V[c] + V[d]
V = [0]*(N+1)
for a, b in R[270]:
    ans += V[a] + V[b]
    V[a] += 1
    V[b] += 1
print(ans)
