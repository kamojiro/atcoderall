from collections import Counter
N = int( input())
S = [ input() for _ in range(N)]
CS = Counter(S)
ans = ""
ansn = 0
for s in CS:
    if CS[s] > ansn:
        ans = s
        ansn = CS[s]
print(ans)









