from itertools import accumulate
N, K = map( int, input().split())
S = input()
D = [0]*N
for i in range(N)    :
    if S[i] == "(":
        D[i] = 1
    else:
        D[i] = -1
AD = list( accumulate([0]+D))
AD.sort( reverse = True)
ans = 0
for i in range(K):
    ans += AD[i]
print(ans)
