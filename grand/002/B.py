N, M = map( int, input().split())
now = [1]*N
ans = [0]*N
ans[0] = 1
for _ in range(M):
    x, y = map( int, input().split())
    x, y = x-1, y-1
    if ans[x] == 1:
        if now[x] >= 2:
            ans[y] = 1
        else:
            ans[x] = 0
            ans[y] = 1
    now[y] += 1
    now[x] -= 1
print( sum( ans))
