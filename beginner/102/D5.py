from itertools import accumulate
from bisect import bisect

def half(T, h):
    b = bisect(T,h)
    if abs(T[b-1]*2 - T[-1] - T[0]) <= abs(T[b]*2 - T[-1] - T[0]):
        return T[b-1] - T[0], T[-1]-T[b-1]
    return T[b] - T[0], T[-1]-T[b]
N = int( input())
A = list( map( int, input().split()))
S = [0] + list( accumulate(A))
ans = 10**9+1
for i in range(2, N-1):
    x, y = half(S[:i+1], S[i]//2)
    z, w = half(S[i:], (S[i] + S[-1])//2)
    m = min(x,y,z,w)
    M = max(x,y,z,w)
    if M-m < ans:
        ans = M-m
print(ans)
