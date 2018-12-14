a, b = input().split()
c = int(a+b)
ans = 'No'
for i in range(1,321):
    if i**2 == c:
        ans = 'Yes'
        break
print(ans)
