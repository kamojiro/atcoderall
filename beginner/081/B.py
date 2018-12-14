N = int(input())
A = list(map(int,input().split()))
ans = 29
for x in A:
    cnt = 0
    for i in range(ans):
        if x % 2 == 0:
            x = x//2
            cnt += 1
        else:
            break
    ans = min(ans,cnt)
print(ans)
