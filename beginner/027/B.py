#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    if sum(A)%N != 0:
        print(-1)
        return
    t = sum(A)//N
    now = 0
    ans = 0
    cnt = 0
    for a in A:
        now += a
        cnt += 1
        if now%cnt == 0 and now//cnt == t:
            now = 0
            cnt = 0
        else:
            ans += 1
    print(ans)
if __name__ == '__main__':
    main()
