N = int( input())
T, A = map( int, input().split())
H = list( map( int, input().split()))
ans = 1
now = abs(T - 0.006*H[0] - A)
for i in range(1,N):
    if abs(T - H[i]*0.006 -A) < now:
        ans = i+1
        now = abs(T - H[i]*0.006 - A)
print(ans)
