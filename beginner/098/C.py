from collections import Counter
N = int(input())
S = list(input())
WL = [0]*(N+1)
for i in range(0,N):
    if S[i] == 'W':
        WL[i+1] = WL[i] + 1
    else:
        WL[i+1] = WL[i]
T = S[::-1]
ER = [0]*(N+1)
for i in range(0,N):
    if T[i] == 'E':
        ER[i+1] = ER[i] + 1
    else:
        ER[i+1] = ER[i]
ans = N
for i in range(N):
    ans = min(ans,WL[i]+ER[N-i-1])
print(ans)
