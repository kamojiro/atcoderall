N = int(input())
P = list( map( int, input().split()))
P.insert(0,0)
ans = 0
cnt = 0
for i in range(1,N+1):
    if P[i] == i:
        cnt += 1
        if cnt == 2:
            ans += 1
            cnt = 0
    elif cnt == 1:
        ans += 1
        cnt = 0
if cnt == 1:
    ans += 1
print(ans)
    
