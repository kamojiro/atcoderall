l, N = map( int, input().split())
X = [ int( input()) for _ in range(N)]
L = [0]*(N+1)
R = [0]*(N+1)
RX = [ l - X[i] for i in range(N-1,-1,-1)]
for i in range(N):
    L[i+1] = L[i]*2 + X[i]
    R[i+1] = R[i]*2 + RX[i]

#初めの位置から右左に順番に往復する場合
print(L)
print(R)
ans = L[N//2] + R[(N+1)//2]
print(ans)
    
