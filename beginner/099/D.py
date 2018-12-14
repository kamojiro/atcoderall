from collections import Counter
N, C = map(int, input().split())
R = [[0]*C]*C
for i in range(C):
    *R[i], = map(int, input().split())
A = [0]*N
L0, L1, L2 = [], [], []
for i in range(N):
    *A, = map(int, input().split())
    for j in range(N):
        if (i+j+2)%3 == 0:
            L0 += [A[j]]
        elif (i+j+2)%3 == 1:
            L1 += [A[j]]
        else:
            L2 += [A[j]]
CL0 = Counter(L0)
CL1 = Counter(L1)
CL2 = Counter(L2)
K = 10**9
for i in range(1,C+1):
    for j in range(1,C+1):
        for k in range(1,C+1):
            if i == j or j == k or k == i:
                pass
            else:
                Y = 0
                for n in range(1,C+1):
                    Y += R[n-1][i-1]*CL0[n]
                for l in range(1,C+1):
                    Y += R[l-1][j-1]*CL1[l]
                for m in range(1,C+1):
                    Y += R[m-1][k-1]*CL2[m]
                K = min(K,Y)
    
print(K)
