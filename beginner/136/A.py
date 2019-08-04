#import sys
#input = sys.stdin.readline
def main():
    a, b, c = map( int, input().split())
    if c <= a-b:
        print(0)
    else:
        print(c-(a-b))
if __name__ == '__main__':
    main()
