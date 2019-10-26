#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    ans = 0
    d = list( map( int, input().split()))
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            ans += d[i]*d[j]
    print(ans//2)
if __name__ == '__main__':
    main()
