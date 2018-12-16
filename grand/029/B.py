from collections import defaultdict
N = int( input())
A = list( map( int, input().split()))
V = [0]*N
ans = 0
for i in range(31,0,-1):
    D = defaultdict( lambda:[])
    T = 2**i
    for j in range(N-1,-1,-1):
        if V[j] == 1:
            continue
        if A[j] < T:
            if D[T - A[j]]:
                ans += 1
                V[D[T-A[j]].pop()]=1
                V[i] = 1
            else:
                D[A[j]].append(j)
print(ans)
