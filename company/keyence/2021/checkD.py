#import sys
#input = sys.stdin.readline
def main():
    Z = int( input())
    A = [ list(input()) for _ in range(Z)]
    N = int(input("N"))
    K = 2**N
    B = [[0]*K for _ in range(K)]
    for k in range(Z):
        for i in range(K-1):
            for j in range(i+1,K):
                if A[k][i] == A[k][j]:
                    B[i][j] += 1
                    B[j][i] += 1
    print(B)
if __name__ == '__main__':
    main()
