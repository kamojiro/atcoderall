#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    N = int( input())
    D = list( map( int, input().split()))
    M = int( input())
    T = list( map( int, input().split()))
    probs = defaultdict( int)
    for d in D:
        probs[d] += 1
    for t in T:
        if probs[t] == 0:
            print("NO")
            return
        probs[t] -= 1
    print("YES")
if __name__ == '__main__':
    main()
