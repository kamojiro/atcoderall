#import sys
#input = sys.stdin.readline

Q = 10**9+7

def getInv(N):
    inv = [0] * (N + 1)
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q % i]) % Q
    return inv

def main():

    n, a, b = map( int, input().split())
    Inv = getInv(2*10**5)
    def cmb(n,r):
        ret = 1
        for i in range(r):
            ret *= n-i
            ret %= Q
            ret *= Inv[i+1]
            ret %= Q
        return ret
    print( (pow(2,n,Q) - cmb(n,a) - cmb(n,b)-1)%Q)
if __name__ == '__main__':
    main()
