#import sys
#input = sys.stdin.readline
from math import pi, cos, sqrt
def main():
    A, B, H, M = map( int, input().split())
    ans = A**2 + B**2 - 2*A*B*cos((M/60 - (H/12+M/(12*60)))*2*pi)
    print(sqrt(ans))
if __name__ == '__main__':
    main()








