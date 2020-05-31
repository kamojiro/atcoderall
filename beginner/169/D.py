#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    N = int( input())
    d = defaultdict( int)
    for i in range(2, int(N**(1/2))+1):
        while N%i == 0:
            d[i] += 1
            N //= i
    if N > 1:
        d[N] += 1
    ans = 0
    for key in d:
        for i in range(1, 100):
            if i*(i+1)//2 > d[key]:
                ans += i-1
                break
    print(ans)
if __name__ == '__main__':
    main()
