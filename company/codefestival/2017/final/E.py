from itertools import accumulate
S = list( input())
N = int( input())
L = len(S)
V = [0]*(L+1)
S = [ ord(S[i]) for i in range(L)]
for _ in range(N):
    l, r = map( int, input().split())
    V[l-1] += 1
    V[r] -= 1
D = list( accumulate(V))
a = ord("a")

for i in range(L):
    S[i] = ( S[i] - a + D[i])%26
ans = "YES"
for i in range(L):
    if not S[i] == S[-1-i]:
        ans = "NO"
        break
print(D)
print(S)
print(ans)
