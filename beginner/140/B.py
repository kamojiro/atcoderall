#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    B = list( map( int, input().split()))
    C = list( map( int, input().split()))
    now = A[0]
    ans = sum(B)
    for i in range(1, N):
        if now + 1 == A[i]:
            ans += C[now-1]
        now = A[i]
    print(ans)
if __name__ == '__main__':
    main()
