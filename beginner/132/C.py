#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    D = list( map( int, input().split()))
    D.sort()
    ans = 0
    if D[N//2] != D[N//2-1]:
        ans = D[N//2] - D[N//2-1]
    print(ans)
if __name__ == '__main__':
    main()








