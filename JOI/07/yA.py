K = int(input())
ans = 0
K = 1000 - K
Koka = [500,100,50,10,5,1]
for yen in Koka:
    a = K//yen
    ans += a
    K -= a*yen
print(ans)
