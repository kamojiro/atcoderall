#import sys
#input = sys.stdin.readline
def getInv(N,Q):
    inv = [0] * (N + 1)
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q % i]) % Q
    return inv

def getCmb(N,Q):
    inv = getInv(N,Q)
    nCr = [1] * (N + 1)
    for i in range(1, N + 1):
        nCr[i] = (nCr[i - 1] * (N - i + 1) * inv[i]) % Q
    return nCr


def main():
    p = int( input())
    A = list( map( int, input().split()))
    ANS = [A[0]]
    pm1Ck = getCmb(p-1,p)
    Pow = [[0]*p for _ in range(p+1)]
    for i in range(p+1):
        Pow[i][0] = 1
    for i in range(1,p):
        for k in range(p-1):
            Pow[i][k+1] = Pow[i][k]*i%p
    for k in range(1,p):
        now = 0
        for i in range(p):
            now -= A[i]*Pow[p-i][p-1-k]*pm1Ck[k]
#            now -= A[i]*pow(p-i,p-1-k,p)*pm1Ck[k]
            now %= p
        ANS.append(now)
    print( " ".join( map( str, ANS)))
    # for i in range(p):
    #     now = 0
    #     for k in range(p):
    #         now += ANS[k]*pow(i,k,p)
    #         now %= p
    #     print(A[i], now)
if __name__ == '__main__':
    main()
