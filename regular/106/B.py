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
    if find(A,x) > find(A,y):
        bx, by = find(A,y), find(A,x)
    else:
        bx, by = find(A,x), find(A,y)
    A[y] = bx
    A[by] = bx

def main():
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    V = [i for i in range(N)]
    CD = [ tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
    for c, d in CD:
        union(V,c,d)
    SA = [0]*N
    SB = [0]*N
    for i in range(N):
        SA[find(V,i)] += A[i]
        SB[find(V,i)] += B[i]
    for i in range(N):
        if SA[i] != SB[i]:
            print("No")
            return
    print("Yes")
    
    
if __name__ == '__main__':
    main()
