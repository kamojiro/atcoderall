def getInv(N):
    nums = [1]*(N + 1)
    inv = [0]*(N + 1)
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q % i]) % Q
        nums[i] = nums[i-1]*i%Q
    return nums, inv

K, N = map( int, input().split())
Q = 998244353
fuct, invs = getInv(N+K)
L = K-1
for t in range(2, 2*K+1):
    ans = 0
    if t%2 == 1:
        p = t//2
        for q in range(p+1):
            if q > N:
                continue
            ans += (fuct[p]*invs[q]*invs[p-q]%Q)*(fuct[N+K-p-q]*invs[N-q]*invs[K-p-1]%Q)
            ans %= Q
    else:
        p = t//2-1
        for q in range(p+1):
            if q == L:
                continue
            print(N-q)
            print(fuct[N-q])
            print(fuct[N-q]*invs[N-q]%Q)
            ans += (fuct[p]*invs[q]*invs[p-q]%Q)*(fuct[N+L-p-q-1]*invs[N-q]*invs[L-p-1]%Q)
            ans %= Q
        ans += fuct[N+K-3]*invs[N-1]*invs[K-2]
        ans %= Q
    print(ans)
