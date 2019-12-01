#import sys
#input = sys.stdin.readline

def main():
    N = int( input())
    S = list( map( int, list( input())))
    T = [[0]*N for _ in range(10)]
    for i in range(N):
        T[S[i]][i] = 1;
    for i in range(10):
        for j in range(N-1):
            T[i][j+1] += T[i][j]
    ANS = [0]*1000
    for m in range(1, N-1):
        for i in range(10):
            for j in range(10):
                if (T[i][m-1] > 0) and (T[j][N-1] - T[j][m] > 0):
                    ANS[100*i + 10*S[m] + j] = 1


    print( sum(ANS))
if __name__ == '__main__':
    main()
