N = int(input())
A = list(map(int, input().split()))
r = 0
now = 0
ans = 0
for i in range(N):
    while N > r:
        if now & A[r] != 0:
            break
        now += A[r]
        r += 1
    now -= A[i]
    ans += r-i
print(ans)    
