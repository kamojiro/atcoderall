from bisect import bisect_left, bisect_right
Q = 10**9+7
N, M = map( int, input().split())
A = list( map( int, input().split()))
B = list( map( int, input().split()))
A.sort()
B.sort()
ans = 1
for i in range(N*M,-1,-1):
    if A[bisect_left(A,i)] == A[i] and B[ bisect_left(B,i)] == B[i]:
        pass
    elif A[bisect_left(A,i)] == A[i]:
        ans *= M - bisect_left(B,i)
    elif B[ bisect_left(B,i)] == B[i]:
        ans *= N - bisect_left(A,i)
    else:
        print((M - bisect_left(B,i)),(N - bisect_left(A,i)), - i + M*N)
        ans *= (M - bisect_left(B,i))*(N - bisect_left(A,i)) - i + M*N
    ans %= Q
print(ans)
