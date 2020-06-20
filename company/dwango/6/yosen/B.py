#import sys
#input = sys.stdin.readline
from itertools import accumulate
Q = 10**9+7

def getFactorials(N):
    ret = [0]*(N+1)
    ret[0] = 1
    for i in range(1, N+1):
        ret[i] = ret[i-1]*i%Q
    return ret

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
    N = int( input())
    X = list( map( int, input().split()))
    if N == 2:
        print(X[0])
        return
    factorials = getFactorials(N)
    combs = getCmb(N-1)
    accX = list( accumulate(X))
    # print(accX)
    ans = 0
    for i in range(N-1):
        z = X[N-1] - X[N-2-i]
        c = factorials[N-2-i]*combs[i+1]%Q*factorials[i]%Q
        ans += z*c%Q
        ans %= Q
        # print(i, "hashi", z, c, z*c)
        if i == N-2:
            continue
        x = (accX[N-1] - accX[i]) - (accX[N-2-i]) - z
        y = factorials[N-3-i]*combs[i+2]%Q*factorials[i]%Q
        # print(i, x, y)
        ans += x*y%Q
        ans %= Q
        # (N-k-1)!*C(N-1,k)*(k-2)!
    print(ans)
    
if __name__ == '__main__':
    main()
