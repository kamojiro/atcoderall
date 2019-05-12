from collections import defaultdict
from bisect import bisect_left, bisect_right
N, Q = map( int, input().split())
A = list( map( int, input().split()))
A.sort()
d = defaultdict( int)
for a in A:
    d[a] += 1
for _ in range(Q):
    L, R, X = map( int, input().split())
    l = bisect_left(A, L)
    r = bisect_right(A, R)
    now = l
    cnt = 0
    ans = 0
    while now <= r-1:
        if d[A[now]]%2 == 1:
            ans ^= A[now]
        cnt += d[A[now]]
        d[A[now]], now = 0, now + d[A[now]]
    print(ans)
    A = A[:l] + A[r:]
    x = bisect_left(A, X)
    A = A[:x] + [X]*(cnt%2) + A[x:] 
    d[X] += cnt%2
