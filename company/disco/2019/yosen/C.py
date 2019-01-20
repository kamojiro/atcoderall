Q = 10**9+7
N = int( input())
ans = 0
for i in range(1, N+1):
    ans +=  (pow(i,10,Q)-pow(i-1,10,Q))*pow(N//i,10,Q)
    ans %= Q
print(ans)
