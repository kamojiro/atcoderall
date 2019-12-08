#import sys
#input = sys.stdin.readline
Q = 10**9 + 7
def main():
    N = int( input())
    A = list( map( int, input().split()))
    T = [[0]*60 for _ in range(N)]
    P = [0]*60
    for i in range(N):
        a = A[i]
        for j in range(60):
            T[i][j] = a%2
            P[j] += a%2
            a //= 2
    ans = 0
    for i in range(60):
        plus = P[i]
        minus = N - plus
        ans = (ans + plus*minus%Q*pow(2,i,Q))%Q
    print(ans)
        
if __name__ == '__main__':
    main()
