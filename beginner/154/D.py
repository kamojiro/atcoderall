#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    P = list( map( int, input().split()))
    now = sum(P[:K])
    ans = now
    for i in range(K,N):
        now -= P[i-K]
        now += P[i]
        if now > ans:
            ans = now
    print((ans+K)/2)
if __name__ == '__main__':
    main()
