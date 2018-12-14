N = int(input())
K = int(input())
X = list( map( int, input().split()))
ans = 0
for i in range(N):
    ans += min(abs(X[i]),abs(X[i]-K))*2
print(ans)
