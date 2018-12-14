N, M = map( int, input().split())
ans = 1
for i in range(1, N):
    if M%i == 0 and M//i >= N:
        ans = max( ans, i)
for i in range(N,int(M**(0.5))+2):
    if M%i == 0:
        ans = max( max( ans, i), M//i)
        break
print(ans)

