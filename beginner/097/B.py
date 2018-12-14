X = int(input())
Y = int(X**(1/2))
ans = 0
for b in range(1,Y+1):
    for p in range(2, 11):
        if b**p <= X:
            ans = max(ans, b**p)
print(ans)
        
    








