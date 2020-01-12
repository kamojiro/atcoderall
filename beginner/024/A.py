#import sys
#input = sys.stdin.readline
def main():
    a, b, c, k = map( int, input().split())
    s, t = map( int, input().split())
    ans = s*a + t*b
    if s+t >= k:
        ans -= c*(s+t)
    print(ans)
if __name__ == '__main__':
    main()








