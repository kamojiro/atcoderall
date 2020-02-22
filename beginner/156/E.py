#import sys
#input = sys.stdin.readline
Q = 10**9+7
def getInv(N):#Qはmod
    inv = [0] * (N + 1)
    inv[0] = 1
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q%i]) % Q
    return inv

def getFactorialInv(N):
    inv = [0] * (N + 1)
    inv[0] = 1
    inv[1] = 1
    ret = [1]*(N+1)
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q%i]) % Q
        ret[i] = ret[i-1]*inv[i] % Q
    return ret

def getFactorial(N):
    ret = [1]*(N+1)
    for i in range(2,N+1):
        ret[i] = ret[i-1]*i%Q
    return ret

def main():
    n, k = map( int, input().split())
    fact = getFactorial(n)
    invfact = getFactorialInv(n)
    if k >= n-1:
        ans = 1
        for i in range(1,n*2):
            ans *= i
            ans %= Q
        print( ans*invfact[n-1]%Q*invfact[n]%Q)
        return
    ans = 0
    for i in range(k+1):
        ans += fact[n]*invfact[i]%Q*invfact[n-i]%Q*fact[n-1]%Q*invfact[i]%Q*invfact[n-1-i]%Q
        ans %= Q
    print(ans)
if __name__ == '__main__':
    main()
