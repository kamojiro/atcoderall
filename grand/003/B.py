N = int( input())
A = [ int( input()) for _ in range(N)]
now = 0
ans = 0
for i in range(N):
    a = A[i]
    if now == 1:
        if a >= 1:
            ans += 1
            a -= 1
    now = 0
    ans += a//2
    a = a - a//2*2
    if a == 1:
        now = 1
print( ans)
