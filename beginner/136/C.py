#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    H = list( map( int, input().split()))
    h = H[-1]
    ans = "Yes"
    for i in range(N-1):
        if h >= H[-i-2]:
            h = H[-i-2]
            continue
        if h + 2 <= H[-i-2]:
            ans = "No"
            break
    print(ans)
if __name__ == '__main__':
    main()
