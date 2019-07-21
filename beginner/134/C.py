import sys
input = sys.stdin.readline
def main():
    N = int( input())
    A = [ int( input()) for _ in range(N)]
    B = [0]*N
    C = [0]*N
    B[0] = A[0]
    C[N-1] = A[N-1]
    for i in range(N-1):
        B[i+1] = max(B[i], A[i+1])
        C[N-2-i] = max( C[N-1-i], A[N-2-i])
    print(C[1])
    for i in range(1, N-1):
        print( max(B[i-1], C[i+1]))
    print(B[N-2])
if __name__ == '__main__':
    main()
