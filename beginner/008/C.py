#import sys
#input = sys.stdin.readline
from math import factorial
def main():
    N = int( input())
    C = [ int( input()) for _ in range(N)]
    ans = 0
    for c in C:
        now = -1
        for i in range(N):
            if c%C[i] == 0:
                now += 1
            ans += factorial(N-now-1)*(N-now)*
if __name__ == '__main__':
    main()
