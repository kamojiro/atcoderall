from collections import defaultdict
N, P = map( int, input().split())
A = defaultdict( int)
S = set()
ans = 1
if N == 1:
    ans = P
else:
    T = P
    for i in range(2, int(P**(1/2)) + 1):
        while P%i == 0:
            P //= i
            S.add(i)
            A[i] += 1
    if T == P:
        A[T] += 1
        S.add(T)
    for s in S:
        if A[s] >= N:
            ans *= s**(A[s]//N)
print(ans)
