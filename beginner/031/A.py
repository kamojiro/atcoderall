#import sys
#input = sys.stdin.readline
def main():
    A, D = map( int, input().split())
    if (A+1)*D >= A*(D+1):
        A += 1
    else:
        D += 1
    print(A*D)
if __name__ == '__main__':
    main()
