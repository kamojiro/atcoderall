K = int(input())
T = [int(input()) for _ in range(K)]
x = 0
y = 0
for t in T:
    if t == 1:
        x += 1
    elif t == 2:
        y += 1
    elif t == 3:
        x = x+y
    else:
        y = x+y
print(x, y)
