import sys
from collections import defaultdict
input = sys.stdin.readline
def main():
    N = int( input())
    A = [ int( input()) for _ in range(N)]
    B = sorted(A)
    d = defaultdict( int)
    for i in range(N):
        d[B[i]] = i
    odd = 0
    for i in range(N):
        if (i+1)%2 == d[A[i]]%2 and d[A[i]]%2 == 1:
            odd += 1
    print(odd)
    
if __name__ == '__main__':
    main()
