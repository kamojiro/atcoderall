#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    Q = 10**9+7
    C = list( map( int, input().split()))
    C.sort()
    ans = 1
    if N == 1:
        print(C[0]*2%Q)
        return
    for i in range(N-1):
        ans += pow(2,i,Q)*(((N-1)-i)*pow(2,N-2-i,Q) + pow(2, N-1-i, Q))*C[i]%Q
        ans %= Q
    ans += pow(2, N-1, Q)*C[N-1]%Q
    ans -= 1
    print(ans*pow(2,N,Q)%Q)
if __name__ == '__main__':
    main()
