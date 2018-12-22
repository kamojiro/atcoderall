N = int( input())
A = list( map( int, input().split()))
ans = 10**6
for a in range(-100, 101):
    cost = 0
    for j in range(N):
        cost += (A[j]-a)**2
    ans = min( ans, cost)
print(ans)
