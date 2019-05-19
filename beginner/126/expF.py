from itertools import permutations
M = int( input())
for m in range(M):
    V = [i for i in range(2**m)]
    V = V+V
    for k in range(2**M):
        check = True
        for P in permutations(V):
            check = True
            C = [-1]*(2**m)
            A = [0]*(2**(m+1))
            A[0] = P[0]
            C[P[0]] = P[0]
            for i in range(1, 2**(m+1)):
                A[i] = A[i-1]^P[i]
                if C[P[i]] == -1:
                    C[P[i]] = A[i]
                else:
                    if A[i]^C[P[i]]^P[i] == k:
                        C[P[i]] = -2
                        continue
                    check = False
                    break
            if check == True:
                # print(P,A,C)
                break
        if check == True:
            print(m,k,P)
            
