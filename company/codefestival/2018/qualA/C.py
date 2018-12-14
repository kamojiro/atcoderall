N, K = map( int, input().split())
A = list( map( int, input().split()))
V = [0]*N
for i in range(N):
    for j in range(61):
        if A[i] < 2**j:
            V[i] = j
            break

