#import sys
#input = sys.stdin.readline
from math import atan, degrees
def main():
    a, b, x = map( int, input().split())
    if (a**2)*b <= 2*x:
        print(-degrees(atan((2*x - (2*a**2*b))/a**3)))
    else:
        print(degrees(atan((b**3/(2*x))**(1/2))))

if __name__ == '__main__':
    main()
