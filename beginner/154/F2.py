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
        ret[i] = ret[i-1]*inv[i]%Q
    return ret

def getFactorial(N):
    ret = [1]*(N+1)
    for i in range(2,N+1):
        ret[i] = ret[i-1]*i%Q
    return ret

def main():
    r1, c1, r2, c2 = map( int, input().split())
    F = getFactorial(2*10**6)
    I = getFactorialInv(10**6)
    ans = 0
    for i in range(c1, c2+1):
        ans += F[i+r2+1]*I[i+1]%Q*I[r2]%Q-1
#        print(i+1, r2,F[i+r2+1]*I[i]%Q*I[r2+1]%Q-1)
        if r1 > 1:
            ans -= F[i+r1]*I[i]%Q*I[r1]%Q-1
        ans %= Q
    print( ans)
if __name__ == '__main__':
    main()
