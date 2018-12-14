N, K = map( int, input().split())
A = [ [0]*2 for _ in range(N)]
for i in range(N):
    A[i] = list(map( int, input().split()))
A.sort()
L = 0
for i in range(N):
    L += A[i][1]
    if L >= K:
        print(A[i][0])
        break
    
