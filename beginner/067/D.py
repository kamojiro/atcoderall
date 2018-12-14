from collections import deque
from copy import deepcopy
N = int( input())
Path = [ [] for _ in range(N)]
for _ in range(N-1):
    a, b = map( int, input().split())
    a, b = a-1, b-1
    Path[a].append(b)
    Path[b].append(a)
Mass = [-1 for _ in range(N)]
F = deque([0])
S = deque([N-1])
while len(F) != 0 or len(S) != 0:
    KF = deque([])
    while len(F) != 0:
        f = F.pop()
        for x in Path[f]:
            if Mass[x] == -1:
                Mass[x] = 1
                KF.append(x)
    F = deepcopy(KF)
    KS = deque([])
    while len(S) != 0:
        s = S.pop()
        for y in Path[s]:
            if Mass[y] == -1:
                Mass[y] = 0
                KS.append(y)
    S = deepcopy(KS)
if sum(Mass) >= N//2+1:
    print('Fennec')
else:
    print('Snuke')
    

