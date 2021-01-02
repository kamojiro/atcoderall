#import sys
#input = sys.stdin.readline
def main():
    H, W = map( int, input().split())
    A = [ list(map(int,input().split())) for _ in range(H)]
    m = min([min(a) for a in A])
    ans = 0
    for aa in A:
        for a in aa:
            ans += a-m
    print(ans)
if __name__ == '__main__':
    main()
