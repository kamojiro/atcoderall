#import sys
#input = sys.stdin.readline
from itertools import product
def main():
    N, K = map( int, input().split())
    D = list( map( int, input().split()))
    NN = list( map( int, str(N)))
    A = [ i for i in range(10) if i not in D]
    ANS = []
    for i in range(1,6):
        for p in product(A, repeat = i):
            now = 0
            for j in range(i):
                now = now*10+p[j]
            if now >= N:
                ANS.append(now)
    print( min(ANS))
if __name__ == '__main__':
    main()
