#import sys
#input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int,input().split()))
    M = 0
    ans = 0
    now = 0
    s = 0
    for a in A:
        if s+a > M:
            M = s+a
        if ans < now + M:
            ans = now+M
        s += a
        now += s
    print(ans)
if __name__ == '__main__':
    main()
