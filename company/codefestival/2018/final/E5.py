from bisect import bisect_right
N, K = map( int, input().split())
A = list( map( int, input().split()))
L = []
ans = 0
for i in range(N):
    a = A[i]
    j = bisect_right(L, a)
    L = L[:j] + [a]*K + L[j:]
    L = L[:K]
    ans += L.pop(0)
print(ans)
