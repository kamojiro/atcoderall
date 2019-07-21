#import sys
#input = sys.stdin.readline
from math import sqrt
def main():
    S = int( input())
    x = 10**9
    y = (S+x-1)//x
    s = 1
    t = x*y-S
    print(0,0,x,s,t, y)
if __name__ == '__main__':
    main()
