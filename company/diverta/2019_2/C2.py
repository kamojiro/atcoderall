N = int( input())
A = list( map( int, input().split()))
A.sort(reverse = True)
plus = 0
zero = 0
for i in range(N):
    if A[i] > 0:
        plus += 1
    elif A[i] == 0:
        zero += 1
minus = N - plus - zero
if plus + zero== N:
    print(sum(A)-A[-1]*2)
    now = A[-1]
    for i in range(N-2):
        print(now, A[i])
        now -= A[i]
    print(A[N-2], now)
elif minus + zero== N:
    print(A[0]*2 - sum(A))
    now = A[0]
    for i in range(1,N):
        print(now, A[i])
        now -= A[i]
elif plus+zero == 1:
    print( sum( list( map( abs, A))))
    now = A[0]
    for i in range(1,N):
        print(now, A[i])
        now -= A[i]
else:
    print( sum( list( map( abs, A))))
    now = A[N-1]
    k = N-1
    for i in range(1,N-1):
        if A[i] <= 0:
            k = i
            break
        print(now, A[i])
        now -= A[i]
    print(A[0], now)
    now = A[0] - now
    for i in range(k,N-1):
        if A[i] > 0:
            pass
        print(now, A[i])
        now -= A[i]
