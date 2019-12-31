import sys
input = sys.stdin.readline
import heapq
def main():
    N, M = map( int, input().split())
    d = dict()
    E = [[] for _ in range(N)]
    for i in range(N-1):
        E[i+1].append(i)
        d[(i+1,i)] = 0
    for _ in range(M):
        l, r, c = map( int, input().split())
        l -= 1
        r -= 1
        E[l].append(r)
        d[(l,r)] = c
    q = [(0,0)]
    heapq.heapify(q)
    path = [10**17]*N
    path[0] = 0
    while q:
        c, v = heapq.heappop(q)
        for e in E[v]:
            if path[e] > c + d[(v,e)]:
                path[e] = c + d[(v,e)]
                heapq.heappush(q, (path[e], e))
    if path[N-1] == 10**17:
        print(-1)
    else:
        print(path[N-1])
if __name__ == '__main__':
    main()
