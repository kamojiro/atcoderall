from bisect import bisect
N, K = map( int, input().split())
X = list( map( int, input().split()))
I = bisect(X, -1)
Xmin = X[:I]
Xmin = [ -x for x in Xmin[::-1]]
Xplu = X[I:]
H = [10**9]*(10**5)
Xmin += H
Xplu += H
ans = 10**9
for i in range( min(I, K)):
    if i == K-1:
        ans = min(ans, Xmin[i])
    else:
        ans = min(ans, Xmin[i]*2 + Xplu[K-i-2])
for i in range( min(N-I, K)):
    if i == K-1:
        ans = min(ans, Xplu[i])
    else:
        ans = min(ans, Xplu[i]*2 + Xmin[K-i-2])
print(ans)
