import sys
input = sys.stdin.readline
from collections import deque
from bisect import bisect_right, bisect_left
def main():
    N = int( input())
    A = [ int( input()) for _ in range(N)]
    d = deque()
    for a in A:
        t = bisect_right(d, a)
        if t == 0:
            d.appendleft(a)
            continue
        if d[t-1] == a:
            t = bisect_left(d, a)
        if t == 0:
            d.appendleft(a)
        else:
            d[t-1] = a
    print(len(d))

if __name__ == '__main__':
    main()
