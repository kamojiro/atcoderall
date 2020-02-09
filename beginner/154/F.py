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
        ret[i] = ret[i-1]*inv[i]
    return ret

def getFactorial(N):
    ret = [1]*(N+1)
    for i in range(2,N+1):
        ret[i] = ret[i-1]*i%Q
    return ret

def main():
    r1, c1, r2, c2 = map( int, input().split())
    F = getFactorial(2*(10**6))
    J = getInv(2*(10**6))
    I = [0]*(10**6+1)
    I[0] = 1
    I[1] = 1
    for i in range(2,10**6+1):
        I[i] = I[i-1]*J[i]%Q
    #print(F[5]*I[5]%Q)
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(1, c2+1):
        a += F[r2+i+1]*I[i+1]%Q*I[r2]%Q-1
#        print(F[r2+i+1]*I[i+1]%Q*I[r2]%Q-1)
        a %= Q
    if r1 == 1:
        b = 0
    else:
        for i in range(1, c2+1):
            b += F[r1+i]*I[i]%Q*I[r1]%Q-1
            b %= Q
    if c1 == 1:
        c = 0
    else:
        for i in range(1, c1):
            c += F[r2+i+1]*I[i+1]%Q*I[r2]%Q-1
            c %= Q
    if c1 == 1 or r1 == 1:
        d = 0
    else:
        for i in range(1, c1):
            d += F[r1+i]*I[i]%Q*I[r1]%Q-1
            d %= Q
#    print(a, b,c, d)
    print((a-b-c+d)%Q)
if __name__ == '__main__':
    main()
