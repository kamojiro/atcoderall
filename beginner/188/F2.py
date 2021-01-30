#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    X, Y = map(int, input().split())
    d = defaultdict(lambda:-1)
    def solve(y):
        if d[y] > -1:
            return d[y]
        if y == 1:
            return abs(X-y)
        if y%2 == 1:
            d[y] = min(abs(X-y),solve((y+1)//2)+2, solve((y-1)//2)+2)
            return d[y]
        d[y] = min(abs(X-y),solve(y//2)+1)
        return d[y]
    print(solve(Y))
if __name__ == '__main__':
    main()
