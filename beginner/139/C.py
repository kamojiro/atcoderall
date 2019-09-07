#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    H = list( map( int, input().split()))
    ans = 0
    now = 0
    height = 10**9+1
    for h in H:
        if height >= h:
            now += 1
            height = h
        else:
            if now > ans:
                ans = now
            now = 1
            height = h
    if now > ans:
        ans = now
    print(ans-1)
if __name__ == '__main__':
    main()
