from itertools import accumulate
N, M = map( int, input().split())
l = 1
r = N
for _ in range(M):
    a, b = map( int, input().split())
    if l <= a:
        l = a
    if b <= r:
        r = b
if r - l >= 0:
    print(r-l+1)
else:
    print(0)

