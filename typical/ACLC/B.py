from itertools import product
def prime_factors(N): #素因数 1を含まないことに注意
    ret = []
    middle = int( N**(1/2))
    tmp = N
    for i in range(2, middle+1):
        if tmp%i == 0:
            t = 1
            while tmp%i == 0:
                tmp //= i
                t *= i
            ret.append(t)
    if tmp != 1:
        ret.append(tmp)
    return ret

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def main():
    N = int( input())
    # print("start")
    P = prime_factors(2*N)
    M = len(P)
    ans = 2*N-1
    # print(M)
    for p in product( range(2), repeat=M):
        x = 1
        for i, t in enumerate(p):
            if t == 1:
                x *= P[i]
        y = N*2//x
        if x == 1:
            if y-1 < ans:
                ans = y-1
            continue
        if y == 1:
            if x-1 < ans:
                ans = x-1
            continue
        _, a, b = xgcd(x,y)
        now = -a*x
        # print(x, y, a, b)
        if a < 0:
            pass
        else:
            now = -b*y
        if now < ans:
            ans = now
    print(ans)
        
        
if __name__ == '__main__':
    main()
