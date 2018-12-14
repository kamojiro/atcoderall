N, C = map( int, input().split())
S = [ list( map( int, input().split())) for _ in range(N)]
X = [0]*(N+1)
RX = [0]*(N+1)
CX = [-C]*(N+1)
RCX = [-C]*(N+1)
now = 0
for i in range(N):
    now += S[i][1]
    X[i+1] = now - S[i][0]
    CX[i+1] = max(X[i+1], CX[i])
now = 0
for i in range(N):
    now += S[N-i-1][1]
    RX[i+1] = now - C + S[N-i-1][0]
    RCX[i+1] = max( RX[i+1], RCX[i])
ans = 0
CX[0] = 0
RCX[0] = 0
RS = S[::-1]
S.insert(0,[0,0])
RS.insert(0,[C,0])
for i in range(N+1):
    ans = max( ans, X[i] + max(RCX[N-i] - S[i][0], 0))
    ans = max( ans, RX[i] + max(CX[N-i] - (C - RS[i][0]),0))
print(ans)
