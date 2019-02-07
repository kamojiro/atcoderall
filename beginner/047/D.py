from collections import defaultdict
N, T = map( int, input().split())
A = list( map( int, input().split()))
now = A[0]
c = 0
for i in range(N):
    c = max( c, A[i]-now)
    now = min( now, A[i])
d = defaultdict( lambda :-1)
for i in range(N):
    d[A[i]] = i
ans = 0
for i in range(N):
    if d[A[i]+c] == -1:
        continue
    if d[A[i]+c] > i:
        ans += 1
print( ans)
