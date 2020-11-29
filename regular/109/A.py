#import sys
#input = sys.stdin.readline
from heapq import heappush, heappop
from collections import defaultdict
def main():
    a, b, x, y = map(int, input().split())
    E = [[] for _ in range(200)]
    N = 100
    d = defaultdict(int)
    for i in range(N-1):
        E[i].append(i+1)
        E[i+1].append(i)
        d[(i,i+1)] = y
        d[(i+1,i)] = y
        E[i+N].append(i+N+1)
        E[i+N+1].append(i+N)
        d[(i+N,i+N+1)] = y
        d[(i+N+1,i+N)] = y
        E[i+N].append(i+1)
        E[i+1].append(i+N)
        d[(i+N,i+1)] = x
        d[(i+1,i+N)] = x
    for i in range(N):
        E[i].append(i+N)
        E[i+N].append(i)
        d[(i,i+N)] = x
        d[(i+N,i)] = x
    a -= 1
    b -= 1
    b += N
    q = [(0,a)]
    visited = [-1]*(N*2)
    while q:
        # print(q)
        z, v = heappop(q)
        if v == b:
            print(z)
            return
        if visited[v] > -1:
            continue
        visited[v] = z
        for w in E[v]:
            if visited[w] == -1:
                heappush(q, (z+d[(v,w)], w))
        
            
        
        
    
if __name__ == '__main__':
    main()
