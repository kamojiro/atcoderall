#import sys
#input = sys.stdin.readline
from itertools import accumulate
def main():
    N, W = map(int,input().split())
    STP = [ tuple(map(int,input().split())) for _ in range(N)]
    L = [0]*(2*10**5+1)
    for s, t, p in STP:
        L[s] += p
        L[t] -= p
    accL = list(accumulate(L))
    if max(accL) <= W:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()
