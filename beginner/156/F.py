#import sys
#input = sys.stdin.readline

from itertools import accumulate

def solve(k, acd, n,x,m):
    now = 0
    cnt = 0
    for p in acd:
        if now+p >= m:
            cnt += 1
        now = p%m
    
def main():
    k, q = map( int, input().split())
    d = list( map( int, input().split()))
    NXM = [ tuple( map( int, input().split())) for _ in range(q)]
    ad = list( accumulate(d))
    ANS = [ solve(d, n, x, m) for n, x, m in NXM]
    print("\n".join( map( str, ANS)))
        
if __name__ == '__main__':
    main()
