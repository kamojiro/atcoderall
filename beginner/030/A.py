#import sys
#input = sys.stdin.readline
def main():
    a, b, c, d = map( int, input().split())
    if a*d == b*c:
        print("DRAW")
    elif a*d < b*c:
        print("TAKAHASHI")
    else:
        print("AOKI")
if __name__ == '__main__':
    main()
