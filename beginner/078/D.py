N, Z, W = map( int, input().split())
A = list( map( int, input().split()))
maxA = max(A)
minA = min(A)
indmax = N-1
indmin = N-1
for i in range(N-1,-1,-1):
    if A[i] == max(A):
        indmax = i
        break
for i in range(N-1,-1,-1):
    if A[i] == min(A):
        indmin = i
        break
if maxA == A[-1]:
    Z = maxA
elif minA == A[-1]:
    Z = maxA
    W = minA
else:
    
