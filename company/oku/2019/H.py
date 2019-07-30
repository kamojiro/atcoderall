#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    A = list( map( int, input().split()))
    ans = 0
    A.sort()
    for i in range(K):
        ans += (A[i]+A[i-K])/A[i-K]
    print(ans)
if __name__ == '__main__':
    main()
