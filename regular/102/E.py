def getInv(N):
    nums = [1]*(N + 1)
    inv = [0] * (N + 1)
    inv[0] = 1
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q % i]) % Q
        nums[i] = nums[i-1]*i%Q
    return nums, inv

K, N = map( int, input().split())
Q = 998244353
fuct, invs = getInv(N+K)
c = fuct[N+K-1]*invs[N]*invs[K-1]%Q
for i in range(2,2*K+1):
    ans = 0
    if i%2 == 1:
        for j in range(1, i//2+1):
            ans += pow(2,j-1,Q)*fuct[N+K-2-j]*invs[K-j]*invs[N-2]
            ans %= Q
    else:
        for j in range(1, i//2):
            ans += pow(2,j-1,Q)*fuct[N+K-2-j]*invs[K-j]*invs[N-2]
            ans %= Q
        k = i//2
        ans += pow(2,k-1,Q)*fuct[N+K-k-2]*invs[K-k]
        ans %= Q
    print((c-ans)%Q)
    
