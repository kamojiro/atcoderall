import sys
input = sys.stdin.readline
def main():
    N = int( input())
    X = []
    for _ in range(N):
        x, l = map( int, input().split())
        X.append((x+l-1, x-l+1))
    X.sort()
    ans = 1
    now = X[0][0]
    for i in range(1,N):
        b, a = X[i]
        if now +1< a:
            now = b
            ans += 1
    print(ans)
    
if __name__ == '__main__':
    main()
