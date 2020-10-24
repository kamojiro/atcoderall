#import sys
#input = sys.stdin.readline
from math import gcd
def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = A[0]
    for a in A:
        ans = gcd(ans,a)
    print(ans)
if __name__ == '__main__':
    main()








