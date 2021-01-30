#import sys
#input = sys.stdin.readline
from heapq import heappush, heappop
def main():
    N = int( input())
    AB = [ tuple(map(lambda x: int(x)-1,input().split())) for _ in range(N)]
    K = 4*10**5
    V = [False]*K
    ANS = [-1]*N
    C = [0]*K
    E = [[] for _ in range(K)]
    h = []
    for i, ab in enumerate(AB):
        a, b = ab
        C[a] += 1
        C[b] += 1
        E[a].append((i, b))
        E[b].append((i,a))
    for i, c in enumerate(C):
        if c > 0:
            heappush(h,(c,i))
    while h:
        c, i = heappop(h)
        if V[i]:
            continue
        if C[i] != c:
            continue
        m = N*2+1
        index = -1

        for j, other_color in E[i]:
            if ANS[j] > -1:
                continue
            if C[other_color] < m:
                m = C[other_color]
                index = j
        if index > -1:
            ANS[index] = i
            V[i] = True
            a, b = AB[index]
            # a or b = i
            C[a] -= 1
            C[b] -= 1
            if not V[a]:
                heappush(h,(C[a],a))
            if not V[b]:
                heappush(h,(C[b],b))
    ans = len(set(ANS))
    # print(ANS)
    for a in ANS:
        if a == -1:
            ans -= 1
            break
    print(ans)
    
if __name__ == '__main__':
    main()
