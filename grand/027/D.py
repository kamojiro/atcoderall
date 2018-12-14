def shaku(K,k,l):
    for m in range(K,10**15+1):
        if m%k == 1 and m%l == 1:
            K = m+1
            return m
            break
N = int( input())
ans = [[0]*N for _ in range(N)]
ans[0][0] = 2
K = 3
for i in range(1,N):
    for j in range(i+1):
        print(ans)
        print(i)
        print(j)
        if j == 0:
            ans[i][0] = shaku(K,ans[i-1][0],ans[i-1][0])
        elif j == i:
            ans[0][j] = shaku(K,ans[0][j-1], ans[0][j-1])
        else:
            ans[i-j][j] = shaku(K, ans[i-j-1][j-1],ans[i-j-1][j])
        K = ans[i-j][j]+1
for j in range(1, N):
    for i in range(N-j):
        print(N-i-1)
        print(j+i)
        ans[N-i-1][j+i] = shaku(K, ans[N-i-2][j+i],ans[N-i-1][j+i+1])
        K = ans[N-i-1][j+N-i-2] + 1
for a in ans:
    print(' '.join( map( str, a)))
