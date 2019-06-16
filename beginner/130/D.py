#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    A = list( map( int, input().split()))
    s = 0
    now = 0
    ans = 0
    for i in range(N):
        now += A[i]
        if now >= K:
            ans += N-i
            now -= A[s]
            s += 1
        else:
            continue
        while now >= K:
            now -= A[s]
            s += 1
            ans += N-i
    print(ans)

if __name__ == '__main__':
    main()
