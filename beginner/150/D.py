def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return(a)

def lcm(a, b):
    return a*b//gcd(a,b)
#import sys
#input = sys.stdin.readline
def main():
    N, M = map( int, input().split())
    A = list( map( int, input().split()))
    B = [a for a in A]
    T = 1
    L = 1
    C = [0]*N
    for i in range(N):
        for _ in range(30):
            if B[i]%2 == 0:
                B[i] //= 2
                C[i] += 1
            else:
                break
    p = C[0]
    for i in range(N-1):
        if p != C[i+1]:
            print(0)
            return
    q = pow(2,p)
    t = 1
    for i in range(N):
        t = lcm(t,A[i]//2)
    if t > M:
        print(0)
        return

    print((M-t)//(t*2) + 1)

if __name__ == '__main__':
    main()

