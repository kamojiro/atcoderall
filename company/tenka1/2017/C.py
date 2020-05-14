#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    for x in range(1,3501):
        if 4*x - N < 0:
            continue
        for y in range(1, 3501):
            if 4*x*y <= N*(x+y):
                continue
            if N*x*y%(4*x*y-N*(x+y)) == 0:
                print(x, y, N*x*y//(4*x*y-N*(x+y)))
                return
if __name__ == '__main__':
    main()
