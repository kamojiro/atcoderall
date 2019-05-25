from collections import defaultdict
d = defaultdict( int)
N = int( input())
ans = 0
for _ in range(N):
    a, b = map( int, input().split())
    if a > b:
        a, b = b, a
    if d[(a,b)] == 0:
        ans += 1
        d[(a,b)] = 1
print( ans)
