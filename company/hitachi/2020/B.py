import sys
input = sys.stdin.readline
def main():
    A, B, M = map( int, input().split())
    a = list( map( int, input().split()))
    b = list( map( int, input().split()))
    X = [ tuple( map( int, input().split())) for _ in range(M)]
    ans = min(a) + min(b)
    for x, y, c in X:
        if a[x-1] + b[y-1] - c < ans:
            ans = a[x-1] + b[y-1] - c
    print(ans)
if __name__ == '__main__':
    main()
