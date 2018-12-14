N, K, Q = map(int, input().split())
*A, = map(int, input().split())
B = sorted(A)
if K != 1:
    print(B[N-1]-B[Q+1])
else:
    
