ans = 10**6
n = int( input())
for i in range(1,n+1):
    if (n-n//i*i) + abs(n//i-i) < ans:
        ans = (n-n//i*i) + abs(n//i-i)
print(ans)
