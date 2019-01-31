from collections import Counter
N = int( input())
C = Counter( input())
ANS = [0]*4
for i in range(4):
    ANS[i] = C[ str(i+1)]
print( max( ANS), min(ANS))
