from itertools import accumulate
N = int( input())
A = list( map( int, input().split()))
AA = list(accumulate(A))
ANS = abs( AA[0]*2 - AA[-1])
for i in range(N-1):
    K = abs( AA[i]*2 - AA[-1])
    ANS = min( K, ANS)
print(ANS)
    
