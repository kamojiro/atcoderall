#import sys
#input = sys.stdin.readline
def main():
    a, b = map( int, input().split())
    if a > 0:
        print("Positive")
        return
    if a <= 0 and b >= 0:
        print("Zero")
        return
    if (b-a+1)%2 == 0:
        print("Positive")
    else:
        print("Negative")
if __name__ == '__main__':
    main()
