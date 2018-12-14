N = int( input())
F = [0]*(N+1)
Q = 10**9 + 7
for i in range(1,N+1):
    n = i
    for j in range(2, int( N**(1/2))+1):
        while n%j == 0:
            F[j] += 1
            n //= j
    if n != 1:
        F[n] += 1
ans = 1
for i in range(N+1):
    ans *= F[i]+1
    ans %= Q
print(ans)
