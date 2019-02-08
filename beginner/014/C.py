from itertools import accumulate
ANS = [0]*(10**6+2)
n = int( input())
for _ in range(n):
    a, b = map( int, input().split())
    ANS[a] += 1
    ANS[b+1] -= 1
print( max( list( accumulate(ANS))))
