D, N = map( int, input().split())
T = [ int(input()) for _ in range(D)]
mM = []
C = []
for _ in range(N):
    a, b, c = map( int, input().split())
    mM.append([a,b])
    C.append(c)
t = T[0]
Cminnow = 100
Cmaxnow = 0
for i in range(N):
    if mM[i][0] <= t and t <= mM[i][1]:
        Cminnow = min( Cminnow, C[i])
        Cmaxnow = max( Cmaxnow, C[i])
ansmin = 0
ansmax = 0
for i in range(1,D):
    t = T[i]
    Cmin = 100
    CMax = 0
    for j in range(N):
        if mM[j][0] <= t and t <= mM[j][1]:
            Cmin = min(Cmin, C[j])
            CMax = max(CMax, C[j])
    print("{} {}".format(Cmin,CMax))
    if abs(CMax - Cminnow) >= abs(Cmin - Cminnow):
        ansmin += abs(CMax - Cminnow)
        Cminnow = CMax
    else:
        ansmin += abs(Cmin - Cminnow)
        Cminnow = Cmin
    if abs(CMax - Cmaxnow) >= abs(Cmin - Cmaxnow):
        ansmax += abs(CMax - Cmaxnow)
        Cmaxnow = CMax
    else:
        ansmax += abs(Cmin - Cmaxnow)
        Cmaxnow = Cmin
print(max(ansmin, ansmax))
