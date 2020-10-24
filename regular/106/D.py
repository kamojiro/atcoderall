Q = 998244353
def getInv(N):
    inv = [0] * (N + 1)
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q % i]) % Q
    return inv

def getCmb(N):
    inv = getInv(N)
    nCr = [1] * (N + 1)
    for i in range(1, N + 1):
        nCr[i] = (nCr[i - 1] * (N - i + 1) * inv[i]) % Q
    return nCr

def main():
    N, K = map(int,input().split())
    A = list(map(int,input().split()))
    B = [1]*(N)
    SA = [N]
    for _ in range(K):
        for i, a in enumerate(A):
            B[i] *= a
            B[i] %= Q
        SA.append(sum(B)%Q)
    ANS = []
    invtwo = pow(2,Q-2,Q)
    for x in range(1,K+1):
        ans = 0
        xCi = getCmb(x)
        for i in range((x+1)//2):
            ans += (SA[i]*SA[x-i]%Q - SA[x])%Q*xCi[i]%Q
            ans %= Q
        if x%2 == 0:
            ans += (SA[x//2]*SA[x//2]%Q - SA[x])%Q*invtwo%Q*xCi[x//2]%Q
            ans %= Q
        ANS.append(ans)
        
    print("\n".join(map(str,ANS)))
if __name__ == '__main__':
    main()
