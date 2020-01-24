#import sys
#input = sys.stdin.readline
from collections import defaultdict

def getHeadTail(n):
    tail = n%10
    while n//10 > 0:
        n //= 10
    return n, tail

def main():
    N = int( input())
    d = defaultdict( int)
    for i in range(1, N+1):
        a, b = getHeadTail(i)
        if a == 0 or b == 0:
            continue
        d[(a,b)] += 1
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            ans += d[(i,j)]*d[(j,i)]

    print(ans)
if __name__ == '__main__':
    main()
