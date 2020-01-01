#import sys
#input = sys.stdin.readline
def main():
    N, A, B = map( int, input().split())
    D = []
    for _ in range(N):
        s, d = input().split()
        d = int(d)
        if d < A:
            d = A
        elif d > B:
            d = B
        if s == "East":
            D.append( d)
        else:
            D.append( -d)
    ans = sum(D)
    if ans == 0:
        print(0)
    elif ans > 0:
        print( "East", ans)
    else:
        print("West", -ans)
if __name__ == '__main__':
    main()
