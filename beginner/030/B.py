#import sys
#input = sys.stdin.readline
def main():
    n, m = map( int, input().split())
    n %= 12
    m /= 60
    n += m
    n /= 12
    n *= 360
    m *= 360
    ans = abs(n-m)
    print(min(ans, 360-ans))
    
if __name__ == '__main__':
    main()
