#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    N, M = map( int, input().split())
    d = defaultdict(lambda : -1)
    md = -1
    mn = -1
    G = [-1]*N
    for _ in range(M):
        s, c = map( int, input().split())
        if G[s-1] == -1:
            G[s-1] = c
        else:
            if G[s-1] != c:
                print(-1)
                return
    if M == 0:
        if N == 1:
            print(0)
            return
    if G[0] == -1:
        G[0] = 1
    if G[0] == 0:
        if N == 1:
            print(0)
        else:
            print(-1)
        return
    ans = 0
    for i in range(N):
        if G[i] == -1:
            G[i] = 0
        ans += G[i]*10**(N-1-i)
    print(ans)
if __name__ == '__main__':
    main()
