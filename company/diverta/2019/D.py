from collections import deque
from copy import deepcopy
def factors(N):
    ret = []
    for i in range(2, int(N**(1/2))+1):
        if N%i == 0:
            ret.append([])
            t = 1
            while N%i == 0:
                N //= i
                ret[-1].append(i**t)
                t += 1
    return ret
N = int( input())
F = factors(N)
C = deque([1])

for d in F:
    T = deepcopy(C)
    for t in T:
        for s in d:
            C.append(t*s)

ans = 0
for c in C:
    m = N//c -1
    if m == 0:
        continue
    if N//m == N%m:
        ans += m

print(ans)
