#import sys
#input = sys.stdin.readline
from math import log2
def main():
    H = int( input())
    n = int( log2( H))
    print( pow(2, n+1)-1)
if __name__ == '__main__':
    main()
