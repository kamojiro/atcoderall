#import sys
#input = sys.stdin.readline
from math import log10
def main():
    N = 20
    for i in range(1,N):
        print(log10(pow(10,i)-1))
        print(i,int(log10(pow(10,i)-1)))
if __name__ == '__main__':
    main()
