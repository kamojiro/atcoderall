from collections import defaultdict
N = int( input())
A = list( map( int, input().split()))
d = defaultdict( int)
d[0] = 1
ans = 0
now = 0
for i in range(N):
    now += A[i]
    ans += d[ now]
    d[ now] += 1
print(ans)
