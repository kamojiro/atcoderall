from collections import deque
N = int( input())
P = [0]*N
H = [0]*N
E = [[] for _ in range(N)]
for i in range(1,N):
    P[i], H[i] = map( int, input().split())
    E[P[i]].append(i)
d = deque()
for t in E[0]:
    d.append((t, H[t]))
MV = [0]*N
e = []
while d:
    s, h = d.popleft()
    MV[s] = h
    for t in E[s]:
        d.appendleft((t, min(h, H[t])))
def solve(E, H,P):
    s = 0
    E[s] = [ t for t in E[s] if H[t] != 0]
    m = 10**10
    while len(E[s]) != 0:
        now = E[s][0]
        h = H[now]
        for t in E[s]:
            if h > H[t]:
                now = t
                h = H[now]
        s = now
        m = min(m,h)
        E[s] = [ t for t in E[now] if H[t] != 0]
    while s != 0:
        H[s] -= m
        s = P[s]
while len(E[0]):
    solve(E,H,P)
    ans = 1
for i in range(1, N):
    if H[i] <= 0:
        ans += 1
print(ans)

