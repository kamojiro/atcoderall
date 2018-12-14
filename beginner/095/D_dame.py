from copy import deepcopy
def UPP(A,n):
    A.insert(0,[n,0])
    B = [0]
    for i in range(len(A)-1):
        B.append(A[i+1][1] + B[i] - A[i+1][0] + A[i][0])
        print(B)
    return B

def PLUS(A,c):
    for i in range(len(A)-1):
        A[i][0] += c
    return A

N, C = map(int, input().split())
X = [list(map(int, input().split())) for i in range(N)]
RX = deepcopy(X)
RX = RX[::-1]
for i in range(N):
    RX[i][0] = C - RX[i][0]

ans = 0
for i in range(1,N):
    RXP = PLUS(A = RX, c = X[i-1][0])
    RXP = RXP[:N - i]
    ans = max(ans, UPP(A = X[:i], n = 0)[i] + max(UPP(A = RXP, n = 0)))

for i in range(1,N):
    XP = PLUS(A = X, c = RX[i-1][0])
    XP = XP[:N - i]
    ans = max(ans, UPP(A = RX[:i], n = 0)[i] + max(UPP(A = XP, n = 0)))

ans = max(ans,max(UPP(A = X, n = 0)),max(UPP(A = RX, n = 0)))

print(ans)

    
    
