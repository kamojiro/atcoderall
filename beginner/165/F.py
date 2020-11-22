import sys
input = sys.stdin.readline
from bisect import bisect_left
def main():
    N = int(input())
    A = list(map(int,input().split()))
    E = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(lambda x:int(x)-1,input().split())
        E[u].append(v)
        E[v].append(u)

    arrival_order = []
    visited = [False]*N
    previous = [-1]*N
    stack = [0]
    while stack:
        v = stack.pop()
        if visited[v]:
            continue
        arrival_order.append(v)
        visited[v] = True
        for w in E[v]:
            if visited[w]:
                continue
            stack.append(w)
            previous[w] = v
    
    euler_tour = [0]
    now = 0
    for v in arrival_order[1:]:
        if previous[v] == now:
            now = v
            euler_tour.append(v)
            continue
        while previous[v] != previous[now]:
            euler_tour.append(-1)
            now = previous[now]
        euler_tour.append(-1)
        euler_tour.append(v)
        now = v

    # print(arrival_order)
    # print(euler_tour)
        
    INF = 10**10
    ANS = [0]*N
    dp = [INF]*N
    stack = []
    
    for v in euler_tour:
        if v == -1:
            # print(stack)
            index, prev_value = stack.pop()
            dp[index] = prev_value
            continue
        # print(v,A[v],bisect_left(dp, A[v]+1),dp[:10])
        # print(dp[:10])
        a = A[v]
        i = bisect_left(dp, a+1)
        stack.append((i,dp[i]))
        dp[i] = a
        # print(v,dp[:10])
        ANS[v] = bisect_left(dp,INF-1)

    print("\n".join(map(str,ANS)))
        
if __name__ == '__main__':
    main()
