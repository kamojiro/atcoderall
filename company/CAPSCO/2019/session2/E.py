from collections import deque
import heapq
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
    if len(E[s]) == 0:
        e.append((h,s))
        continue
    for t in E[s]:
        d.appendleft(( min(h, H[t]), t))
def minus(P, MV,H, s, h):
    while s != 0:
        MV[s] -= h
        H[s] -= h
        s = P[s]
def check(P,MV,s):
    ret = True
    while s != 0:
        if MV[s] <= 0:
            ret = False
            break
        s = P[s]
    return ret
heapq.heapify(e)
def adding(e,P,MV,s):
    s = P[s]
    while s != 0:
        if MV[s] <= 0:
            continue
        heapq.heappush(e, (MV[s], s))
        s = P[s]
while e:
    h, s = heapq.heappop(e)
    h = MV[s]
    if check(P, MV,s):
        minus(P,MV,H,s,h)
    if P[s] != 0:
        e.append(P[s])
ans = 1
for i in range(1, N):
    if H[i] <= 0:
        ans += 1
print(ans)
    

        # V = [-1]*N
# V[0] = 0

