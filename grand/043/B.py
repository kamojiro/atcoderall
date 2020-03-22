#import sys
#input = sys.stdin.readline
from collections import Counter
def main():
    N = int( input())
    A = list( map(int, list( input())))
    B = []
    for i in range(N-1):
        B.append( abs( A[i] - A[i+1]))

    C = Counter(B)
    if C[1] > 0:
        if (C[1] - C[0] - C[2])%2 == 0:
            print(1)
        else:
            print(0)
    elif C[2] == 0 or C[2] == N-1:
        print(0)
    else:
        print(2)
            
if __name__ == '__main__':
    main()
