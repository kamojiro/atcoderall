#import sys
#input = sys.stdin.readline
from math import log2
def main():
    N = int( input())
    M = int( log2(N))
    x = 1
    for i in range(M):
        if M%2 == 0:
            if i%2 == 1:
                x = 2*x
            else:
                x = 2*x+1
        else:
            if i%2 == 0:
                x = 2*x
            else:
                x = 2*x+1
    if M%2 == 0:
        if x <= N:
            print("Aoki")
        else:
            print("Takahashi")
    else:
        if x <= N:
            print("Takahashi")
        else:
            print("Aoki")
        
if __name__ == '__main__':
    main()
