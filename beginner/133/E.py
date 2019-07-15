Q = 10**9+7
#import sys
#input = sys.stdin.readline
from collections import deque
def main():
    N, K = map( int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map( lambda x: x-1, map( int, input().split()))
        E[a].append(b)
        E[b].append(a)
    V = [0]*N
    V[0] = K
    d = deque()
    for i in range( len(E[0])):
        t = E[0][i]
        V[t] = K - 1 - i
        if K == i+1:
            print(0)
            return
        cnt = 0
        for v in E[t]:
            if V[v] == 0:
                d.append(v)
                if K == cnt+2:
                    print(0)
                    return
                V[v] = K-2-cnt
                cnt += 1
    while d:
        t = d.popleft()
        cnt = 0
        for v in E[t]:
            if V[v] == 0:
                d.append(v)
                if K == cnt+2:
                    print(0)
                    return
                V[v] = K-2-cnt
                cnt += 1
    ans = 1
    for v in V:
        ans *= v
        ans %= Q
    print(ans)
    
if __name__ == '__main__':
    main()

