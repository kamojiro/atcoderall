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

def solve():
    N, M = map(int,input().split())
    V = [i for i in range(N)]
    for _ in range(M):
        a, b = map(lambda x:int(x)-1,input().split())
        union(V,a,b)
    C = [0]*N
    s = set()
    for i in range(N):
        C[find(V,i)] += 1
        s.add(find(V,i))
    S = list(s)
    one = find(V,0)
    enu = find(V,N-1)
    one_comp = C[one]
    others = N-one_comp
    need = one_comp*(one_comp-1)//2 + others*(others-1)//2-M
    if need%2 == 0:
        return "Second"
    else:
        return "First"
    # odd = 0
    # for t in S:
    #     if t == one or t == enu:
    #         continue
    #     if C[t]%2 == 1:
    #         odd += 1
    # now = C[one]*(C[one]-1)//2 + C[enu]*(C[enu]-1)//2
    # # if now%2 == 0, then second
    # print(now, odd)
    # if (now+odd+M)%2 == 0:
    #     return "Second"
    # else:
    #     return "First"
    
def main():
    T = int(input())
    ANS = [solve() for _ in range(T)]
    print("\n".join(ANS))
    

if __name__ == '__main__':
    main()
