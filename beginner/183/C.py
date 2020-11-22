#import sys
#input = sys.stdin.readline
from itertools import permutations
def main():
    N, K = map(int,input().split())
    T = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for P in permutations(range(1,N)):
        dist = 0
        now = 0
        for p in P:
            dist += T[now][p]
            now = p
        dist += T[P[-1]][0]
        
        if dist == K:
            ans += 1
    print(ans)
if __name__ == '__main__':
    main()
