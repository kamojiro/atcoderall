N, M, X = map(int, input().split())
A = list( map( int, input().split()))
B = [0]*(N+1)
for x in A:
    B[x] = 1
for i in range(N):
    B[i+1] += B[i]
print( min(B[X]-B[0],B[N]-B[X]))
