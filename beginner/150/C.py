#import sys
#input = sys.stdin.readline
from itertools import permutations
def main():
    N = int( input())
    P = list( map( int, input().split()))
    Q = list( map( int, input().split()))
    Pem = list( map( lambda x: list(x), permutations( range(1, N+1))))

    M = 1
    for i in range(1, N+1):
        M *= i
    for i in range(M):
        if Pem[i] == P:
            p = i
        if Pem[i] == Q:
            q = i
    print( abs(p-q))
if __name__ == '__main__':
    main()
