N = int( input())
ANS = [0]*N
for i in range(N):
    a, b = map( int, input().split())
    ANS[i] = a+b
print( max(ANS))
