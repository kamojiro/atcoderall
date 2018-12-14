from bisect import bisect
N = int(input())
X = list(map(int,input().split()))
NX = sorted(X)
a = NX[int(N/2)]
b = NX[int((N-2)/2)]
for i in range(N):
    if bisect(NX,X[i]) <= N/2:
        print(a)
    else:
        print(b)
