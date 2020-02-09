#import sys
#input = sys.stdin.readline
def main():
    H, A = map( int, input().split())
    print((H+A-1)//A)
if __name__ == '__main__':
    main()
