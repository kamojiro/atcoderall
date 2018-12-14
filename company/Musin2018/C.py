N, M = map(int, input().split())
S = [ list(input()) for i in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        U, D, L, R = 0,0,0,0
        if S[i][j] == '#':
            continue
        for k in range(i-1,-1,-1):
            if S[k][j] == '#':
                break
            else:
                U += 1
        for k in range(i+1,N):
            if S[k][j] == '#':
                break
            else:
                D += 1
        for k in range(j-1,-1,-1):
            if S[i][k] == '#':
                break
            else:
                L+= 1
        for k in range(j+1,M):
            if S[i][k] == '#':
                break
            else:
                R += 1
        ans += (L+R)*(D+U)
print(ans)
                
                
