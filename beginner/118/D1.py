N, M = map( int, input().split())
A = list( map( int, input().split()))
C = [0,2,5,5,4,5,6,3,7,6]
dp = [(-1,0)]*(N+1)
for a in A:
    if C[a] <= N:
        dp[C[a]] = (1,1)
Z = list( set( C[a] for a in A))
Z.sort()
for i in range(2,N+1):
    for z in Z:
        if i > z:
            if dp[i-z][0] >= 0:
                if dp[i-z][0] + 1 > dp[i][0]:
                    dp[i] = (dp[i-z][1]+1, i-z)

s = N
ANS = [0]*10
while s != 0:
    _, b = dp[s]
    ANS[s-b] += 1
    s = b
ans = ""
A.sort( key = None, reverse = True)
for a in A:
    ans = ans + str(a)*ANS[C[a]]
    ANS[C[a]] = 0
print( ans)
