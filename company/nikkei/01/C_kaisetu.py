N = int( input())
A = [0]*N
B = [0]*N
S = [(0,0)]*N
for i in range(N):
    a, b = map( int, input().split())
    A[i] = a
    B[i] = b
    S[i] = (-a-b,i)
S.sort()
ansa = 0
ansb = 0
for i in range(N):
    _, j = S[i]
    if i%2 == 0:
        ansa += A[j]
    else:
        ansb += B[j]
print( ansa-ansb)
