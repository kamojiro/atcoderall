Q = 10**9+7
#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    ans = 0
    for i in range(1, int(N**(1/2))+1):
        if N//i == i:
            ans += N//i*2-1
            ans %= Q
            break
        elif N//i < i:
            break
        if i*i <= N:
            ans += N//i*2-1
        else:
            ans += N//i*2
        ans %= Q
    print(ans)
if __name__ == '__main__':
    main()
