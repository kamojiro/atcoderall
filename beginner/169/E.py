import sys
input = sys.stdin.readline
def main():
    N = int( input())
    t = 1
    if N%2 == 0:
        t = 2
    AB = [ tuple( map( lambda x: int(x)*t, input().split())) for _ in range(N)]
    A = [ab[0] for ab in AB]
    B = [ab[1] for ab in AB]
    A.sort()
    B.sort()
    if t == 1:
        m = A[N//2]
        M = B[N//2]
    else:
        m = (A[N//2-1]+A[N//2])//2
        M = (B[N//2-1]+B[N//2])//2
    print(M-m+1)
if __name__ == '__main__':
    main()
