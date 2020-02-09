import sys
input = sys.stdin.readline

def fft(f:list, inverse:int) -> list:
    from math import log2, cos, sin, pi
    deg = len(f)
    if deg == 1:
        return f
    N = int( log2( deg-1))+1
    f += [0]*( pow(2,N) - deg)
    zeta = 1 # 2^N-th root of unity
    before = f
    twopow = 1
    zetai = 1
    for n in range(1,N+1):
        after = []
        I = pow(2,n)
        J = pow(2,N-n)
        zeta = complex(cos(2*pi/I), inverse*sin(2*pi/I))
        diff = pow(2, N-n)
#        print(I, J)
        for i in range(I):
            bi = i%(I//2)*J*2
            if i == 0:
                zetai = 1
            else:
                zetai *= zeta
#            zetai = pow(zeta, i)
            for j in range(J):
                after.append(before[bi + j] + before[bi + j + J]*zetai)
        before = after
    return after

def convolution(f,g):
    from math import log2
    n = len(f)
    m = len(g)
    if n == 1 and m == 1:
        return [f[0]*g[0]]
    l = int( log2( n+m-1))+1
    pl = pow(2,l)
    f += [0]*(pl-n)
    g += [0]*(pl-m)
    Ff = fft(f,1)
    Fg = fft(g,1)
    FfFg = [ Ff[i]*Fg[i] for i in range(pl)]
    #return list( map(lambda x:int( x.real+0.4), map(lambda x: x/pl, fft(FfFg, -1)[:n+m-1])))
    return list( map(lambda x:int( x.real+0.4), map(lambda x: x/pl, fft(FfFg, -1)[1:n+m-1])))

def main():
    N = int( input())
    A = [0]
    B = [0]
    for _ in range(N):
        a, b = map( int, input().split())
        A.append(a)
        B.append(b)
    # A = [0]*(N+1)
    # B = [0]*(N+1)
    # for i in range(N):
    #     A[i+1], B[i+1] = map( int, input().split())
    print( "\n".join( map( str, convolution(A,B))))
    # P = convolution(A,B)
    # for i in range(1, 2*N+1):
    #     print(P[i])
if __name__ == '__main__':
    main()
