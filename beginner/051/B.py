K, S = map( int, input().split())
ans = 0
for i in range(K+1):
    for j in range(K+1):
        if i+j <= S and i+j+K>=S:
            ans += 1
print(ans)
