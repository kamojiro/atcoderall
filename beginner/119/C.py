N, A, B, C = map( int, input().split())
T = [A,B,C]
L = [ int( input()) for _ in range(N)]
L.sort( key = None, reverse = True)
ans = 10**4
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if i == k or j == k:
                continue
            C = [(L[i], 0), (L[j],1), (L[k],2)]
            print(C)
            nowans = 0
            for m in range(N):
                if m == i or m == j or m == k:
                    continue
                for v in range(3):
                    l, p = C[v]
                    if T[p] - l > abs(T[p] - l - L[m]) + 10:
                        C[v] = (l+L[m], p)
                        nowans += 10
                C.sort( key = None, reverse = True)
            print(C)
            for v in range(3):
                nowans += abs( C[v][0] - T[ C[v][1]])
            ans = min( ans, nowans)
print( ans)
            

