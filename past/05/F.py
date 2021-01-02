#import sys
#input = sys.stdin.readline
from itertools import product
def main():
    N, M = map( int, input().split())
    ABC = [ tuple( map( lambda x: int(x)-1, input().split())) for _ in range(M)]
    J = [[] for _ in range(N)]
    for a, b, c in ABC:
        J[a].append((b,c))
        J[b].append((a,c))
        J[c].append((a,b))
    ans = 0
    for p in product(range(2), repeat=N):
        now = 0
        for x in range(N):
            if p[x] == 1:
                continue
            for y,z in J[x]:
                if p[y] == 1 and p[z] == 1:
                    now += 1
                    break
        if ans < now:
            ans = now
    print(ans)
    
if __name__ == '__main__':
    main()
