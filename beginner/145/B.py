#import sys
#input = sys.stdin.readline
from math import factorial, sqrt
from itertools import permutations
def main():
    N = int( input())
    V = [ tuple( map( int, input().split())) for _ in range(N)]
    ans = 0
    for P in permutations( range(N)):
        for i in range(N-1):
            ans += sqrt( (V[P[i]][0] - V[P[i+1]][0])**2 + (V[P[i]][1] - V[P[i+1]][1])**2)

    print( ans/ factorial(N))
if __name__ == '__main__':
    main()
