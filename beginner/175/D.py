#import sys
#input = sys.stdin.readline
from itertools import accumulate
def solve(P, C, K, Checked, s):
    B = []
    B.append( C[s])
    now = P[s]
    Checked[s] = True
    while now != s:
        B.append(C[now])
        Checked[now] = True
        now = P[now]
    sumB = sum(B)
    L = len(B)
    accB = [0] + list( accumulate(B))
    ret = B[0]
    for i in range(L):
        for j in range(i+1,L+1):
            if j - i > K:
                continue
            if accB[j] - accB[i] > ret:
                ret = accB[j] - accB[i]
    accRB = [0] + list( accumulate(B[::-1]))
    # print(B, accB, accRB)
    # print(ret)
    for i in range(L+1):
        for j in range(L+1):
            if i==0 and j==0:
                continue
            if i + j > K:
                continue
            t = accB[i] + accRB[j]
            if sumB > 0:
                t += (K-(i+j))//L*sumB
            if t > ret:
                ret = t
                # print(i,j,ret)
    return ret
        
    
def main():
    N, K = map( int, input().split())
    P = list( map( lambda x: int(x)-1, input().split()))
    C = list( map( int, input().split()))
    Checked = [False]*N
    ans = C[0]
    for s in range(N):
        if Checked[s]:
            continue
        ans_s = solve(P, C, K, Checked, s)
        if ans_s > ans:
            ans = ans_s
    print(ans)
if __name__ == '__main__':
    main()
