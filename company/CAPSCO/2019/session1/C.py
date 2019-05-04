from itertools import combinations
from collections import defaultdict
N, K = map( int, input().split())
A = list( map( int, input().split()))
M = defaultdict( int)
for i in range(5):
    M[str(i)] = i
for i in range(5,10):
    M[str(i)] = i - 4
ans = 10000
for C in combinations( range(N), K):
    price = sum([ A[k] for k in C])
    now = sum([M[s] for s in str( price)])
    if now < ans:
        ans = now
print(ans)
