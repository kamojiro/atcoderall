N = int( input())
S = list( map( int, input().split()))
A = list( map( int, input().split()))
T = [0]*N
for i in range(N):
    T[i] = S[i]*A[i]
print( max(T))
