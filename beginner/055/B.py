N = int( input())
ans = 1
Q = 10**9+7
for i in range(1,N+1):
    ans = ans*i%Q
print(ans)
