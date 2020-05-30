#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    T = int( input())
    for _ in range(T):
        N, A, B, C, D = map( int, input().split())
        d = defaultdict( lambda : 10**30+10)
        
if __name__ == '__main__':
    main()
