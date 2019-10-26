N, X = map( int, input().split())
A = list( map( int, input().split()))

m = max(A)
ans = 0
for a in A:
    if a+X >= m:
        ans += 1
print(ans)










