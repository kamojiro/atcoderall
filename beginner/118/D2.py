N, M = map( int, input().split())
A = list( map( int, input().split()))
Needs = [0,2,5,5,4,5,6,3,7,6]
A.sort(reverse = True)
V = [0]*10
Check = []
for a in A:
    if V[Needs[a]] == 0:
        Check.append(Needs[a])
        V[Needs[a]] = a
Check.sort()
dp = [-100000]*(N+1)
dp[0] = 0

for x in Check:
    if x <= N:
        dp[x] = 1
for i in range(1,N):
    t = dp[i]
    for x in Check:
        if x + i <= N:
            if dp[x+i] < t + 1:
                dp[x+i] = t+1
ans = ""
t = N
W = [0]*10
while t > 0:
    for a in A:
        x = Needs[a]
        if t-x>=0:
            if dp[t-x]+1 == dp[t]:
                W[V[x]] += 1
                t -= x
                break
for i in range(9,0,-1):
    ans += str(i)*W[i]
print(ans)
