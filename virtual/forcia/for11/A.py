#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    N = int( input())
    A = list( map( int, input().split()))
    d = defaultdict( int)
    for a in A:
        d[a] += 1
    ans = 0
    for key, value in d.items():
        if key > value:
            ans += value
        elif key < value:
            ans += value - key
    print(ans)
if __name__ == '__main__':
    main()
