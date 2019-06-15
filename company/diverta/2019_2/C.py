N = int( input())
B = list( map( int, input().split()))
B.sort(reverse=True)
plus = 0
for i in range(N):
    if B[i] > 0:
        plus += 1
minus = N - plus
adding = 0
if plus <= minus:
    adding -= sum(B[plus*2:])
    A = B[:plus*2]
else:
    A = B

if plus == 0 or plus == 1:
    print(-sum(B)+B[0]*2)
    now = B[0]
    for a in B[1:]:
        print(now, a)
        now -= a
elif plus <= minus:
    N, K = plus*2, N
    print( sum(A[:N//2]) - sum(A[N//2:]) + adding)
    now = A[0]
    print(now, A[N-1])
    now -= A[N-1]
    for i in range(2,N):
        if i%2 == 0:
            print(A[N-1-i//2], now)
            now = A[N-1-i//2] - now
        else:
            print(A[i//2], now)
            now = A[i//2] - now
    for a in B[plus*2:]:
        print(now, a)
        now -= a
    
elif N%2 == 0:
    print( sum(A[:N//2]) - sum(A[N//2:]))
    now = A[0]
    print(now, A[N-1])
    now -= A[N-1]
    for i in range(2,N):
        if i%2 == 0:
            print(A[N-1-i//2], now)
            now = A[N-1-i//2] - now
        else:
            print(A[i//2], now)
            now = A[i//2] - now
else:
    print( sum(A[:N//2+1]) - sum(A[N//2+1:]))
    now = A[N-1]
    print(now, A[0])
    now -= A[0]
    for i in range(2, N):
        if i%2 == 0:
            print(A[i//2], now)
            now = A[i//2] - now
        else:
            print(A[N-1-i//2], now)
            now = A[N-1-i//2] - now
