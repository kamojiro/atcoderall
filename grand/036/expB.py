#import sys
#input = sys.stdin.readline
from collections import defaultdict, deque
def main():
    n, k = map( int, input().split())
    A = list( map( int, input().split()))
    q = deque()
    d = defaultdict( int)
    for _ in range(k):
        for a in A:
            if d[a] == 0:
                q.append(a)
                d[a] = 1
                continue
            d[a] = 0
            while q:
                t = q.pop()
                d[t] = 0
                if t == a:
                    break
        print(q)

if __name__ == '__main__':
    main()
