N, x = map( int, input().split())
A = list( map( int, input().split()))
ans = 0
Sums = 0
A.sort()
for i in range(N-1):
    Sums += A[i]
    if Sums > x:
        break
    ans += 1
Sums += A[N-1]
if Sums == x:
    ans += 1
print(ans)
    
