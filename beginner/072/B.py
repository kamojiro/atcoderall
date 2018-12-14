from collections import deque
S = list(input())
ans = ''
cnt = 0
for x in S:
    if cnt == 0:
        ans += x
    cnt = (cnt+1)%2
print(ans)
