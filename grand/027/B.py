N, X = map( int, input().split())
G = list( map( int, input().split()))
ans = 0
nowd = 0
nowg = 0
for i in range(N):
    if i == 0:
        nowd = G[i]
        nowg += 1
        ans += G[i]
    else:
        if ((nowg + 1)**2) *(G[i]-G[i-1]) + ((nowg+2)**2)*G[i] + X <= ((nowg+1)**2)*G[i-1] + G[i] + 4*G[i] + 2*X:
            ans += ((nowg+1)**2)*(G[i]-nowd)
            nowd = G[i]
            nowg += 1
        else:
            ans += ((nowg+1)**2)*G[i-1] + G[i] + X
            nowd = G[i]
            nowg = 1
    print(ans)
ans += ((nowg + 1)**2)*G[N-1] + X
print(ans)
