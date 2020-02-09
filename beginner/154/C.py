#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    N = int( input())
    A = list( map( int, input().split()))
    d = defaultdict( int)
    for a in A:
        if d[a] == 1:
            print("NO")
            return
        d[a] = 1
    print("YES")
if __name__ == '__main__':
    main()
