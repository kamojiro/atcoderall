N = int( input())
A = [(0,0)]*N
for i in range(N):
    A[i] = ( int( input()), i)
A.sort()
ANS = [0]*N
now = A[0][0]
ans = 0
for i in range(N):
    a, j = A[i]
    if now == a:
        ANS[j] = ans
    else:
        now = a
        ans += 1
        ANS[j] = ans
for i in range(N):
    print( ANS[i])
##print( " ".join( map( str, ANS)))
