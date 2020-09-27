#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    now = 0
    ans = 0
    for a in A:
        if now <= a:
            now = a
            continue
        ans += now - a
    print(ans)
if __name__ == '__main__':
    main()
