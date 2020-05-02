#import sys
#input = sys.stdin.readline
def main():
    K = int( input())
    A, B = map( int, input().split())
    if B//K - (A-1)//K > 0:
        print("OK")
    else:
        print("NG")
if __name__ == '__main__':
    main()
