N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)
A.append(0)
B = [0]
C = [0]
for i in range(N+1):
    C.append(abs(A[i+1] - A[i]))
S = sum(C)
for i in range(N):
    print(S-C[i+1]-C[i+2] + abs(A[i]-A[i+2]))
