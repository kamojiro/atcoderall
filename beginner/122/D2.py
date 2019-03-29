def check(s):
    c = False
    if s[:3] == "AGC" or s[1:] == "AGC" or s[0] + s[2:] == "AGC" or s[:2] + s[3] == "AGC" or s[:3] == "ACG" or s[1:] == "ACG" or s[:3] == "GAC" or s[1:] == "GAC":
        c = True
    return c

from collections import defaultdict
from itertools import product
N = int( input())
Q = 10**9 + 7
dp = [ defaultdict( int) for _ in range(N+1)]

for s in product("AGCT", repeat = 3):
    dp[3]["".join(s)] = 1
ans = 0
for i in range(4, N+1):
    for c in product("AGCT", repeat = 3):
        c = "".join(c)
        for t in "AGCT":
            if check(c+t):
                # print(c+t, dp[i-1][c])
                ans += (dp[i-1][c]*pow(4,N-i,Q))%Q
                ans %= Q
            else:
                dp[i][c[1:]+t] += dp[i-1][c]
                dp[i][c[1:]+t] %= Q
if N == 3:
    ans = 3
print( (pow(4,N,Q) - ans)%Q)
