#import sys
#input = sys.stdin.readline
def main():
    a, b, c, d = map( int, input().split())
    for i in range(300):
        c -= b
        if c <= 0:
            print("Yes")
            return
        a -= d
        if a <= 0:
            print("No")
            return
if __name__ == '__main__':
    main()
