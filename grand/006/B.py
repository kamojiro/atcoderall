#import sys
#input = sys.stdin.readline
from itertools import permutations
def main():
    ret = set()
    N = int( input())
    check = [0 for _ in range(N*2)]
    for p in permutations(range(1,N*2)):
        ret.add(median(p, N*2-1, check))
    print( sorted( list(ret)))
    print( check)
def median(q, n, check):
    t = q;
    p = [ q[i] for i in range(n)]
    while len(p) > 1:
        q = [ med(p[i:i+3]) for i in range(len(p)-2)]
        p = q
    if check[p[0]] == 0:
        print(p[0], t)
        check[p[0]] = 1;

    return p[0]
def med(v):
    return sorted(v)[1]
if __name__ == '__main__':
    main()
