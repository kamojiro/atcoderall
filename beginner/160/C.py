#import sys
#input = sys.stdin.readline
def main():
    K, N = map( int, input().split())
    A = list( map( int, input().split()))
    ans = K - A[0] - (K-A[N-1])
    for i in range(N-1):
        if K - (A[i+1] - A[i]) < ans:
            ans = K - (A[i+1] - A[i])
    print(ans)
if __name__ == '__main__':
    main()
