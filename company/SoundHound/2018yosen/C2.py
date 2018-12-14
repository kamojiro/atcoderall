n, m, d = map(int, input().split())
if d == 0:
    C = n
else:
    C = 2*(n-d)
print(C*(m-1)/n**2)


