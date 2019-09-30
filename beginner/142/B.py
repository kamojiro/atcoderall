#import sys
#input = sys.stdin.readline
def main():
    N, K = map( int, input().split())
    H = list( map( int, input().split()))
    ans = 0
    for h in H:
        if h >= K:
            ans += 1
    print(ans)
if __name__ == '__main__':
    main()








