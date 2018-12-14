L = sorted(list(map(int,input().split())))
a = L[2] - L[0]
b = L[2] - L[1]
if a%2 == 0 and b%2 == 0:
    ans = (a + b)/2
elif a%2 == 1 and b%2 == 1:
    ans = (a + b)/2
else:
    ans = (a + b + 1)/2 + 1
print(int(ans))

