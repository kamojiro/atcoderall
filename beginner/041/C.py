N = int( input())
A = [(0,0)]*N
B = list( map( int, input().split()))
for i in range(N):
    A[i] = (B[i], i+1)
A.sort( key=None, reverse=True)
for i in range(N):
    print(A[i][1])
