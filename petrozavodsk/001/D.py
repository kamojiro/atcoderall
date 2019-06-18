def find(A,x):
    p = A[x]
    if p == x:
        return x
    a = find(A,p)
    A[x] = a
    return a
 
def union(A, x, y):
#    bx, by = sorted([find(A,x), find(A,y)]) # bx, by = find(A,x), find(A,y)だと無限ループ。
    if find(A,x) > find(A,y):
        bx, by = find(A,y), find(A,x)
    else:
        bx, by = find(A,x), find(A,y)
    A[y] = bx
    A[by] = bx

#import sys
#input = sys.stdin.readline
import heapq
def main():
    N, M = map( int, input().split())
    A = list( map( int, input().split()))
    V = [ i for i in range(N)]
    q = []
    for _ in range(M):
        x, y = map( int, input().split())
        union(V, x, y)
    C = [0]*N
    T = [ [] for _ in range(N)]
    for i in range(N):
        C[find(V,i)] += 1
        heapq.heappush(T[find(V,i)], A[i])
    ans = 0
    if M == 0 and N == 1:
        print(0)
        return
    if M == 0:
        print("Impossible")
        return
    s = 0
    for i in range(N):
        if C[i] >= 2:
            if s == 0:
                q = T[i]
                heapq.heapify(q)
                s = 1
                continue
            if q:
                ans += heapq.heappop(q)
                ans += heapq.heappop(T[i])
                for a in T[i]:
                    heapq.heappush(q, a)
            else:
                print("Impossible")
                return
    for i in range(N):
        if C[i] == 1:
            if q:
                ans += heapq.heappop(q)
                ans += T[i][0]
            else:
                print("Impossible")
                return
    print(ans)
            
if __name__ == '__main__':
    main()
