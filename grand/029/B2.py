from collections import defaultdict
def twopower(n):
    for i in range(32):
        if n < 2**i:
            return 2**i
N = int( input())
A = list( map( int, input().split()))
d = defaultdict( int)
e = defaultdict( int)
for i in range(N):
    d[A[i]] += 1
A.sort(reverse=True)
i = 0
ans = 0
while i < N:
    if e[A[i]] >= d[A[i]]:
        i += 1
        continue
    e[A[i]] += 1
    L = twopower(A[i]) - A[i]
    if e[L] < d[L]:
        ans += 1
        e[L] += 1
    i += 1
print(ans)
