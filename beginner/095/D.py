N, C = map( int, input().split())
S = [ list( map( int, input().split())) for _ in range(N)]
X = [0]*(N+1)
RX = [0]*(N+1)
CX = [-C]*(N+1)
RCX = [-C]*(N+1)
now = 0
M = -C
m = -C
for i in range(N):
    X[i+1] = X[i] + S[i][1] - S[i][0] + now
    now = S[i][0]
    M = max(M, X[i+1])
    CX[i+1] = M
now = 0
for i in range(N):
    x, v = S[-i-1]
    x = C - x
    RX[i+1] = RX[i] + v - x + now
    now = x
    m = max(m, RX[i+1])
    RCX[i+1] = m
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
