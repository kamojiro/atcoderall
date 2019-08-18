import sys
input = sys.stdin.readline
from random import shuffle
def main():
    N, M = map( int, input().split())
    A = [ list( map( int, input().split())) for _ in range(N)]
    B = [[0]*M for _ in range(N)]
    C = [[0]*M for _ in range(N)]
    NOW = [[0]*M for _ in range(N)]
    for i in range(N):
        T = []
        S = []
        for j in range(M):
            if (A[i][j]-1)//N == i:
                S.append(A[i][j])
            else:
                T.append(A[i][j])
        A[i] = T+S
    for i in range(N):
        T = [0]*M
        for j in range(M):
            a = (A[i][j]-1)//M
            for k in range(M):
                if T[k] != 0:
                    continue
                if NOW[a][k] == 0:
                    B[i][k] = A[i][j]
                    NOW[a][k] = 1
                    T[k] = 1
                    break
 

    for i in range(N):
        for j in range(M):
            C[(B[i][j]-1)//M][j] = B[i][j]

    for i in range(N):
        print(" ".join( map( str, B[i])))
    for i in range(N):
        print(" ".join( map( str, C[i])))        
if __name__ == '__main__':
    main()
