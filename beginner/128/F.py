from collections import defaultdict
N = int( input())
S = list( map( int, input().split()))

ans = 0
for c in range(1,N):
    now = 0
    for t in range(c ,N, c):
        if ((N-1-t)%c == 0 and N-1-t <= t) or N-1-t - c <=0:
            break
        now += S[t] + S[N-1-t]
        if now > ans:
            ans = now
print(ans)
