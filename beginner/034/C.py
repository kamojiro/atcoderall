Q = 10**9+7
#import sys
#input = sys.stdin.readline
def main():
    w, h = map( int, input().split())
    w, h = w-1, h-1
    ans = 1
    for i in range(w+h, w, -1):
        ans *= i
        ans %= Q
    for i in range(1, h+1):
        ans *= pow(i, Q-2, Q)
        ans %= Q
    print(ans)
if __name__ == '__main__':
    main()
