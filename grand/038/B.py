import sys
input = sys.stdin.readline
from heapq import heapify, heappop, heappush
def main():
    N, K = map( int, input().split())
    P = list( map( int, input().split()))
    ans = 0
    now = -1
    cnt = 1
    CNT = [0]*N
    for i in range(N-1,-1,-1):
        p = P[i]
        if p < now:
            cnt += 1
        else:
            cnt = 1
        now = p
        if cnt >= K:
            CNT[i] = 1
    if sum(CNT) > 0:
        ans = 1
            
    for i in range(K-1):
        if P[i] > P[i+1]:
            ans += 1
            break
    Max = [ -P[i] for i in range(K)]
    Min = [ P[i] for i in range(K)]
    heapify(Max)
    heapify(Min)
    C = [0]*N
    for i in range(K, N):
        while C[Min[0]] == 1:
            heappop(Min)
        while C[-Max[0]] == 1 or Max[0] == -P[i-K]:
            heappop(Max)
        # print(C, Max)
        # print(P[i+1-K])
        # print(P[i-K], Min[0], P[i] , -Max[0])
        if CNT[i+1-K] == 1:
            pass
        elif P[i-K] == Min[0] and P[i] > -Max[0]:
            pass
        else:
            ans += 1
        C[P[i-K]] = 1
        heappush(Min, P[i])
        heappush(Max, -P[i])
    print(ans)
    
if __name__ == '__main__':
    main()
