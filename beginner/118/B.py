N, M = map( int, input().split())
ANS = [1]*(M+1)
ANS[0] = 0
for _ in range(N):
    C = list( map( int, input().split()))[1:]
    for i in range(1, M+1):
        if i in C:
            pass
        else:
            ANS[i] = 0
print( sum(ANS))
