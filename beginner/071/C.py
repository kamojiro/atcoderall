from collections import defaultdict
N = int( input())
A = list( map( int, input().split()))
D = defaultdict(lambda: 0)
ansL = 0
ansS = 0
for a in A:
    D[a] += 1
    if D[a] == 2:
        if a >= ansL:
            ansL, ansS = a, ansL
        else:
            ansS = max( ansS, a)
    if D[a] == 4:
        if a >= ansL:
            ansL, ansS = a, a
        else:
            ansS = max( ansS, a)
print(ansL*ansS)
