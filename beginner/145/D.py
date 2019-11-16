#import sys
#input = sys.stdin.readline
def main():
    Q = 10**9+7
    X, Y = map( int, input().split())
    if (X+Y)%3 != 0:
        print(0)
        return
    H = (X+Y)//3
    if (X < H) or (Y < H):
        print(0)
        return
    N = X+Y - (X+Y)//3*2
    K = X -N
    L = Y-N
    ans = 1
    s = 1
    t = 1
    for i in range(1, N+1):
        ans *= i
        ans %= Q
    for i in range(1, K+1):
        s *= i
        s %= Q
    for i in range(1, L+1):
        t *= i
        t %= Q
    ans *= pow(s, Q-2, Q)
    ans %= Q
    ans *= pow(t, Q-2, Q)
    ans %= Q
    print(ans)
if __name__ == '__main__':
    main()
