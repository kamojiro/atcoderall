from copy import deepcopy
N = int(input())
L = [[0,0]]*N
for i in range(N):
    L[i] = list(map(int,input().split()))
L = sorted(N)
A = [x[0] for x in L]
B = [x[1] for x in L]
B = sorted(B)
if A[0] < -B[N-1]:
    C = deepcopy(A)
    A = [-x for x in B[::-1]]
    B = [-x for x in A[::-1]]
    L = sorted([[-x[0],-x[1]] for x in L])



