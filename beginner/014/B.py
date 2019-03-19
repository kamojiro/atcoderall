n, X = map( int, input().split())
A = list( map( int, input().split()))
ans = 0
i = 0
while X > 0:
    if X%2 == 1:
        ans += A[i]
    X //= 2
    i += 1
print( ans)
