import sys
input = sys.stdin.readline
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

def main():
    n, m, K = map( int, input().split())
    V = [0]*n
    W = [0]*n
    for i in range(n):
        W[i], V[i] = map( int, input().split())
    A = [i for i in range(n)]
    for _ in range(m):
        a, b = map( int, input().split())
        a, b = a-1, b-1
        union(A, a, b)
    for i in range(n):
        v = find(A, i)
        if V[i] == -1:
            continue
        for j in range(i+1, n):
            if v == find(A, j):
                V[i] += V[j]
                V[j] = -1
                W[i] += W[j]
    dp = [0]*(K+1)
    for i in range(n):
        if V[i] == -1:
            continue
        v, w = V[i], W[i]
        for j in range(K, w-1, -1):
            if dp[j] < dp[j-w] + v:
                dp[j] = dp[j-w] + v
    print(max(dp))
    
if __name__ == '__main__':
    main()

