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
    F = getFactorial(2*10**6+2)
    I = getFactorialInv(10**6+1)

    def G(a, b):
        return F[a+b+2]*I[a+1]%Q*I[b+1]%Q
    
    print( ( G(r2,c2) - G(r2, c1-1) - G(r1-1, c2) + G(r1-1, c1-1))%Q)
if __name__ == '__main__':
    main()
