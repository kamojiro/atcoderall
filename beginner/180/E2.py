#import sys
#input = sys.stdin.readline

def main():
    N = int(input())
    XYZ = [ tuple(map(int,input().split())) for _ in range(N)]
    dist = [[0]*N for _ in range(N)]
    INF = 10**10
    dp = [[INF]*(1<<N) for _ in range(N)]
    for i, abc in enumerate(XYZ):
        a, b, c = abc
        for j, pqr in enumerate(XYZ):
            if i == j:
                continue
            p, q, r = pqr
            dist[i][j] = abs(p-a) + abs(q-b) + max(0,r-c)
            if i == 0:
                dp[j][1<<j] = dist[i][j]
    pow2 = [1]
    for _ in range(N-1):
        pow2.append(pow2[-1]*2)
    pows = []
    for i, p in enumerate(pow2):
        if i == 0:
            continue
        pows.append((i,p))

    for k in range(1,1<<N):
        if k%2 == 1:
            continue
        for i, p in pows:
            now = dp[i][k]
            if k&p == 0 or k == p:
                continue
            for j in range(1,N):
                if dp[j][k-p] + dist[j][i] < now:
                    now = dp[j][k-p] + dist[j][i]
            dp[i][k] = now
    # print(dp)
    ANS = []
    # print(dist)
    occ = (1<<N)-1
    # print(cities)
    for i in range(N):
        ANS.append(dp[i][occ-1]+dist[i][0])
    print(min(ANS))

if __name__ == '__main__':
    main()
