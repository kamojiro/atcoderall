N = int( input())
A = list( map( int, input().split()))
B = []
for k in range(1, N+1):
    L = k//2
    for i in range(0, N-k+1):
        C = A[i:i+k]
        C.sort()
        B.append(C[L])
B.sort()
print( B[ ((N+1)*N)//4])
        
