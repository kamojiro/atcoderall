#import sys
#input = sys.stdin.readline
def main():
    S, W = map( int, input().split())
    if S <= W:
        print("unsafe")
    else:
        print("safe")
if __name__ == '__main__':
    main()
