import sys
input = sys.stdin.readline

from collections import defaultdict

def prime_factors(d,N): #素因数 1を含まないことに注意
    ret = []
    middle = int( N**(1/2))
    tmp = N
    for i in range(2, middle+1):
        if tmp%i == 0:
            c = 0
            while tmp%i == 0:
                tmp //= i
                c += 1
            if d[i] < c:
                d[i] = c
    if tmp != 1:
        if d[tmp] == 0:
            d[tmp] = 1

Q = 10**9+7
def main():
    N = int( input())
    A = list( map( int, input().split()))
    d = defaultdict( int)
    for a in A:
        prime_factors(d, a)
    s = 1
    for key, value in d.items():
        s *= pow( key, value)
    ans = 0
    for a in A:
        ans += s*pow(a,Q-2,Q)
    print(ans%Q)
if __name__ == '__main__':
    main()
