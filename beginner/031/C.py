#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    ans = -1000000
    for i in range(N):
        takahashi = 0
        aoki = -100000
        for j in range(N):
            now_takahashi = 0
            now_aoki = 0
            if i == j:
                continue
            l, r = min(i, j), max(i, j)
            for k in range(l, r+1):
                if (k+l)%2 == 1:
                    now_aoki += A[k]
                else:
                    now_takahashi += A[k]
            if aoki < now_aoki:
                aoki = now_aoki
                takahashi = now_takahashi
        if ans < takahashi:
            ans = takahashi
    print(ans)

if __name__ == '__main__':
    main()
