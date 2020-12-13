#import sys
#input = sys.stdin.readline
from math import gcd
def main():
    N = int( input())
    n = 2
    for k in range(2,N+1):
        n = n*k//gcd(n,k)
    print(n+1)
    
if __name__ == '__main__':
    main()
