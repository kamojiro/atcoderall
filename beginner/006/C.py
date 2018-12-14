N = int( input())
W = [ int( input()) for _ in range(N) ]
D = [ 0 for _ in range(N)]
for i in range(N):
    dan = W[i]
    cnt = -1
    difw = 10**5
    Flag = False
    for j in range(N):
        if D[j] == 0 and Flag == False:
            cnt = j
            break
        elif D[j] >= dan:
            Flag = True
            if difw > D[j] - dan:
                difw = D[j] - dan
                cnt = j
    D[cnt] = dan
ans = 0
for i in range(N):
    if D[i] == 0:
        break
    else:
        ans += 1
print(ans)
