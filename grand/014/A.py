#import sys
#input = sys.stdin.readline
from math import gcd
def main():
    a, b, c = map( int, input().split())
    if a == b == c:
        if a%2 == 1:
            print("0")
        else:
            print("-1")
        return
    ans = 0
    bi = 2
    while a%bi == 0 and b%bi == 0 and c%bi == 0:
        a, b, c = a//2+b//2, b//2+c//2, c//2+a//2
        ans += 1
    print(ans)
if __name__ == '__main__':
    main()
