def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

N, M = map( int, input().split())
g = gcd(N,M)
S = input()
T = input()
c = M//g
t = N//g
ans = M*N//g
for i in range(N):
    if c*i%t == 0:
        if S[i] != T[c*i//t]:
            ans = -1
print(ans)
