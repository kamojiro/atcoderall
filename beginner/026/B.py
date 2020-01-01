#import sys
#input = sys.stdin.readline
from math import pi
def main():
    N = int( input())
    R = [ int( input()) for _ in range(N)]
    R.sort(reverse=True)
    R += [0]
    ans = 0
    for i in range(N):
        if i*2+1 > N:
            break
        ans += (R[i*2]**2 - R[i*2+1]**2)*pi
    print(ans)
if __name__ == '__main__':
    main()
