from bisect import bisect_left
from itertools import accumulate
N, Q = map( int, input().split())
A = list( map( int, input().split()))
odd = [0]*N
even = [0]*N
odd[0] = A[0]
accA = [0] + list(accumulate(A))
for i in range(1,N):
    if i%2 == 0:
        odd[i] = odd[i-1] + A[i]
        even[i] = even[i-1]
    else:
        odd[i] = odd[i-1]
        even[i] = even[i-1] + A[i]
if N%2 == 0:
    taka = [0] + even
else:
    taka = [0] + odd
for _ in range(Q):
    x = int( input())
    l= 0
    r = N-1
    while r - l >= 2:
        m = (l+r)//2
        if A[m] < x:
            l = m
            continue
        if m - bisect_left(A, 2*x - A[m]) == N-1-m:
            l = m
            break
        elif m - bisect_left(A, 2*x - A[m]) > N-1-m:
            l = m
        else:
            r = m
    print(l, taka[bisect_left(A, 2*x - A[l], lo =0, hi = N-1)],accA[N] - accA[l])
    if l >= N-1:
        print(taka[N])
    else:
        print( taka[bisect_left(A, 2*x - A[l], lo =0, hi = N-1)] + accA[N] - accA[l])


