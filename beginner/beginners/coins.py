A = int(input()) + 1
B = int(input()) + 1
C = int(input()) + 1
x = int(input())
x = x/50
i = 0
for a in range(A):
    for b in range(B):
        for c in range(C):
            if (a * 10 + b * 2 + c == x):
                i += 1
print(i)
