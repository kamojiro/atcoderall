def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n;

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p;
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result;

N, A, B, K = map(int, input().split())
Q = 998244353
ans = 0
for i in range(N+1):
    for j in range(N+1):
        if A*i + B*j == K:
            ans = (ans + cmb(N,i)*cmb(N,j))%Q
print(ans)
            









