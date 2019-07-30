#import sys
#input = sys.stdin.readline
def main():
    x, y = map( int, input().split())
    if y< 0:
        print(-1)
        return
    if y%2 == 1:
        print(-1)
        return
    f = y//2
    if f%2 == 0:
        if x%2 == 0 and abs(x) <= f:
            print(f)
            return
        print(-1)
        return
    if x%2 == 1 and abs(x) <= f:
        print(f)
        return
    print(-1)
if __name__ == '__main__':
    main()
