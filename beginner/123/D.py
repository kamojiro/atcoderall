X, Y, Z, K = map( int, input().split())
A = list( map( int, input().split()))
B = list( map( int, input().split()))
C = list( map( int, input().split()))
# A.sort( key=None, reverse = True)
# B.sort( key=None, reverse = True)
# C.sort( key=None, reverse = True)
AB = [0]*(X*Y)
for i in range(X):
    for j in range(Y):
        AB[i*Y+j] = A[i]+B[j]
AB.sort( key=None, reverse = True)
ABC = [0]*3000000
for i in range( min(X*Y, 3000)):
    for j in range(Z):
        ABC[i*Z + j] = AB[i]+C[j]
ABC.sort( key=None, reverse = True)
for i in range(K):
    print( ABC[i])
