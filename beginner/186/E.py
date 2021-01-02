#import sys
#input = sys.stdin.readline
from math import gcd

def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

def solve():
    N, S, K = map( int, input().split())
    g = gcd(N,K)
    if (N-S)%g > 0:
        return -1
    m = (N-S)//g
    N //= g
    K //= g
    # print("N-S", "g",N-S, g)

    _, x, y = extgcd(K,N)
    # print(K, N, m)
    # print(x, y)
    x *= m
    return x - x//N*N
    
    

def main():
    T = int( input())
    ANS = [solve() for _ in range(T)]
    print("\n".join(map(str, ANS)))
if __name__ == '__main__':
    main()
