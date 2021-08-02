from collections import deque
def main():
    N = int( input())
    P = [0] + list(map(lambda x: int(x)-1,input().split()))
    E = [[] for _ in range(N)]
    for v in range(1,N):
        E[P[v]].append(v)
    # visited = [False]*N
    # visited[0] = True
    d = deque([0])
    H = []
    while d:
        v = d.popleft()
        H.append(v)
        for w in E[v]:
            d.append(w)
    V = [1]*N
    for v in H[::-1]:
        if v == 0:
            continue
        V[P[v]] += V[v]
    # print(V)
    dp = [[1,0] for _ in range(N)]
    # dp[i][0]: 1st
    for v in H[::-1]:
        if not E[v]:
            continue
        # even1st = 0
        # even2nd = 0
        # odds = 0
        Deven = []
        D = []
        for w in E[v]:
            # if V[w] % 2 == 0:
            #     even1st += dp[w][0]
            #     even2nd += dp[w][1]
            # else:
            #     odds ^= 1
            if (dp[w][0] <= dp[w][1]) and V[w]%2 == 0:
                Deven.append(w)
            else:
                D.append((dp[w][0]-dp[w][1], w))
        # dp[v][0^odds] = 
        # D.sort()
        for w in Deven:
            dp[v][0] += dp[w][0]
            dp[v][1] += dp[w][1]
        F = deque(sorted(D))
        turn = 1
        for z, w in D:
            if V[w] % 2 == 0:
                dp[v][turn] += dp[w][0]
                dp[v][turn^1] += dp[w][1]
            else:
                dp[v][turn] += dp[w][0]
                dp[v][turn^1] += dp[w][1]
                turn ^= 1
                    
            # dp[v][turn] += dp[w][0]
            # dp[v][turn^1] += dp[w][1]
            # turn ^= 1
    # print(dp)
    print(dp[0][0])
        
    
    
if __name__ == '__main__':
    main()
