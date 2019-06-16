#import sys
#input = sys.stdin.readline
def main():
    N, X = map( int, input().split())
    L = list( map( int, input().split()))
    ans = 1
    now = 0
    for i in range(N):
        now += L[i]
        if now > X:
            break
        ans += 1
    print(ans)
        
if __name__ == '__main__':
    main()







