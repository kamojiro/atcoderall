N, A, B = map( int, input().split())
X = list( map( int, input().split()))
now = X[0]
ans = 0
for i in range(1,N):
    x = X[i]
    if (x-now)*A >= B:
        ans += B
    else:
        ans += A*(x-now)
    now = x
print(ans)









