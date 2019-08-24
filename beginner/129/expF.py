#import sys
#input = sys.stdin.readline
from numpy import matrix, eye, dot
def modMatrix(N, A, Q): #N×N行列のmod
    for i in range(N):
        for j in range(N):
            A[i,j] %= Q
    return

def main():
    N = 3
    X = [[i+j for j in range(N)] for i in range(N)]
    A = matrix(X)
    modMatrix(3, A, 4)
    print(X)
    print(A)
if __name__ == '__main__':
    main()
