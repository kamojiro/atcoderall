#import sys
#input = sys.stdin.readline
def main():
    N, K = map(int,input().split())
    ans = 0
    for s in range(2,2*N+1):
        if 2 <= K+s and K+s <= 2*N:
            ans += (N-abs(s-(N+1)))*(N-abs((K+s)-(N+1)))
    print(ans)
if __name__ == '__main__':
    main()
