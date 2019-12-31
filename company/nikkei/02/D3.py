import sys
input = sys.stdin.readline
import heapq
def main():
    N, M = map( int, input().split())
    d = dict()
    E = [[] for _ in range(N)]
    for i in range(N-1):
        E[i+1].append((0,i))
    for _ in range(M):
        l, r, c = map( int, input().split())
        l -= 1
        r -= 1
        E[l].append((c,r))
    q = [(0,0)]
    heapq.heapify(q)
    path = [-1]*N
    while q:
        c, v = heapq.heappop(q)
        if path[v] >= 0:
            continue
        path[v] = c
        for cost, e in E[v]:
            if path[e] == -1:
                heapq.heappush(q, (c+cost, e))
    print(path[-1])
if __name__ == '__main__':
    main()
