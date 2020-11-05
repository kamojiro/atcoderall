#import sys
#input = sys.stdin.readline
import numpy
def main():
    N, K = map(int,input().split())
    mat = np.matrix([[0]*(N+1) for _ in range(N+1)])
    mat[k][0] = 1
    for i in range(1,N+1):
        for j in range(1,N+1):
            mat[i][] += 1
if __name__ == '__main__':
    main()
