N, M = map( int, input().split())
X = [(0,0,0)]*M
Y = [1]*(N+1)
for i in range(M):
    p,y = map( int, input().split())
    X[i] = (y,p,i)
X.sort()
ANS = ['']*M
for i in range(M):
    y, p, j = X[i]
    ans = '%06d'%p + '%06d'%Y[p]
    ANS[j] = ans
    Y[p] += 1
for i in range(M):
    print(ANS[i])

