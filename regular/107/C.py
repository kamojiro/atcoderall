Q = 998244353

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

def factorial(N):
    ret = [1]
    for i in range(1,N+1):
        ret.append(ret[-1]*i%Q)
    return ret
    
def main():
    N, K = map(int,input().split())
    A = [ list(map(int,input().split())) for _ in range(N)]
    G = [ i for i in range(N)]
    R = [ j for j in range(N)]
    
    for i in range(N-1):
        for j in range(i+1,N):
            t = True
            for k in range(N):
                if A[i][k]+A[j][k] > K:
                    t = False
                    break
            if t:
                union(G,i,j)
            t = True
            for k in range(N):
                if A[k][i]+A[k][j] > K:
                    t = False
                    break
            if t:
                union(R,i,j)

    factorials = factorial(N)
    VG = [0]*N
    VR = [0]*N
    for i in range(N):
        VG[find(G,i)] += 1
        VR[find(R,i)] += 1
    ans = 1
    for g in VG:
        ans *= factorials[g]
        ans %= Q
    for r in VR:
        ans *= factorials[r]
        ans %= Q
    print(ans)
if __name__ == '__main__':
    main()
