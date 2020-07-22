#import sys
#input = sys.stdin.readline
def main():
    a, b, x = map( int, input().split())
    print(b//x - (a-1)//x)
if __name__ == '__main__':
    main()
