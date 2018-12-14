from collections import Counter
N = int(input())
S = []
T = []
for i in range(N):
    S.append(input())
M = int(input())
for i in range(M):
    T.append(input())
ans = 0
#SS = set(S)|set(T)
CS = Counter(S)
CT = Counter(T)
A = [0]
for x in CS:
    if CS[x] > CT[x]:
        A.append(CS[x]-CT[x])
print(max(A))
    
