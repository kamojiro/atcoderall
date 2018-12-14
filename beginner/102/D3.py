import bisect as bisect
N = int(input())
*A, = map(int, input().split())
B = [0]
for x in A:
    B.append(B[-1]+x)

ans = 10**15
for i in range(2, N-1):
    print(i)
    m = sum(A[:i])/i
    M = sum(A[i:])/(N-i)
    n = bisect.bisect(B,m)
    l = bisect.bisect(B,M)
    if abs(B[i]-B[n]-B[n]+B[0]) <= abs(B[i]-B[n-1]-B[n-1]+B[0]):
        C = abs(B[i]-B[n])
        D = abs(B[n]-B[0])
    else:
        C = abs(B[i]-B[n-1])
        D = abs(B[n-1]-B[0])
    if abs(B[N]-B[l]-B[l]+B[i]) <= abs(B[N]-B[l-1]-B[l-1]+B[i]):
        E = abs(B[N]-B[l])
        F = abs(B[l]-B[i])
    else:
        E = abs(B[N]-B[l-1])
        F = abs(B[l-1]-B[i])
    print([C,D,E,F])
    ans = min(ans, max([C,D,E,F])-min([C,D,E,F]))
print(ans)
    

