import heapq
from collections import deque
N, Q = map( int, input().split())
H = [(0,0,0) for _ in range(N)]
for i in range(N):
    s, t, x = map( int, input().split())
    H[i] = (x-t+1, x-s, x)
D = [ ( -int( input()), i) for i in range(Q)]
D.sort()
H.sort()
d = deque(H)
q = []
ANS = [0]*Q
for i in range(Q):
    t, j = D[i]
    while d:
        if d[0][0] <= t:
            _, s, x = d.popleft()
            heapq.heappush(q,(x,s))
        else:
            break
    while q:
        if q[0][1] >= t:
            break
        heapq.heappop(q)
    if not q:
        ANS[j] = -1
    else:
        ANS[j] = q[0][0]
for ans in ANS:
    print( ans)
