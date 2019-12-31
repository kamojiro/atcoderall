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
    path = [10**17]*N
    path[0] = 0
    while q:
        _, v = heapq.heappop(q)
        for cost, e in E[v]:
            if path[e] > path[v] + cost:
                path[e] = path[v] + cost
                heapq.heappush(q, (path[e], e))
    if path[N-1] == 10**17:
        print(-1)
    else:
        print(path[N-1])
if __name__ == '__main__':
    main()
