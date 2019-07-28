#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    B = list( map( int, input().split()))
    ans = 0
    for i in range(N):
        if B[i] > A[i]:
            B[i] -= A[i]
            ans += A[i]
        else:
            ans += B[i]
            B[i] = 0
        if B[i] > A[i+1]:
            ans += A[i+1]
            A[i+1] = 0
        else:
            A[i+1] -= B[i]
            ans += B[i]
    print(ans)
if __name__ == '__main__':
    main()

