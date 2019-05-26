N, M = map( int, input().split())
A = list( map( int, input().split()))
T = [(0,0)]*M
for i in range(M):
    b, c = map( int, input().split())
    T[i] = (c,b)
T.sort(reverse = True)
D = [-1]*N
cnt = 0
for i in range(M):
    c, b = T[i]
    for _ in range(b):
        D[cnt] = c
        cnt += 1
        if cnt >= N:
            break
    if cnt >= N:
        break
A.sort()
for i in range(N):
    if D[i] == -1:
        break
    if D[i] > A[i]:
        A[i] = D[i]
    else:
        break
print( sum(A))
