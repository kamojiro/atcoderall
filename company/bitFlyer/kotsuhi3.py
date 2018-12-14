import bisect as bisect
N, Q = map(int, input().split())
*X, = map(int, input().split())
kX = [0]
for x in X:
    kX.append(kX[-1] + x)
XR = [10**9-x for x in X]
lX = [0]
for x in XR:
    lX.append(lX[-1] + x)
print(lX)
for i in range(1,Q+1):
    C, D = map(int, input().split())
    l = bisect.bisect(X,C)
    ld = bisect.bisect(X,C+D)
    lb = bisect.bisect(X,C-D)
    print("{}""{}""{}".format(l,ld,lb))
    K = D*(N-ld+lb)
    print(K)
    K += kX[ld] - kX[l] - (ld-l)*C
    print(K)
    K += lX[l] - lX[lb] + (lb-l)*(10**9-C)
    print(K)
