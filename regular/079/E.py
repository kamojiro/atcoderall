def solve(A, N):
    ret = 0
    while max(A) > N-1:
        for i in range(N):
            if A[i] > N-1:
                t = A[i]//N
                for j in range(N):
                    if j == i:
                        A[j] -= t*N
                        continue
                    A[j] += t
                ret += t
    return ret
N = int( input())
A = list( map( int, input().split()))
ans = 0
for i in range(N):
    if A[i] > N-1:
        t = A[i]//N
        for j in range(N):
            if j == i:
                A[j] -= t*N
                continue
            A[j] += t
        ans += t
for i in range(N):
    if A[i] > N+1:
        t = A[i]//(N+1)
        if A[i] - t*(N+1) <= N-1:
            t -= 1
        A[i] -= t*(N+1)
        ans += t*(N+1)
print( ans + solve(A,N))
