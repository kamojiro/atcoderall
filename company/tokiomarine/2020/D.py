import sys
input = sys.stdin.readline
from math import log2
def main():
    N = int( input())
    VW = [ tuple( map( int, input().split()))]
    Q = int( input())
    vL = [ tuple( map( int, input().split())) for _ in range(Q)]
    for v, L in vL:
        dp = [0]*(L+1)
        while v > 0:
            
if __name__ == '__main__':
    main()
