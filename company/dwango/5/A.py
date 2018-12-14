N = int( input())
A = list( map( int, input().split()))
m = sum(A)/N
ans = 0
now = 1000
for i in range(N):
    if abs(m-A[i]) < now:
        ans = i
        now = abs(m-A[i])
print(ans)










