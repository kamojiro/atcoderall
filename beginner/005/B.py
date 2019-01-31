N = int( input())
ans = 100
for _ in range(N):
    a = int( input())
    if a < ans:
        ans = a
print( ans)
