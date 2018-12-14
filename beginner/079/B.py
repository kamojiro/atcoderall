N = int(input())
a = 2
b = 1
if N == 1:
    print(1)
else:
    for _ in range(N-1):
        a, b = b, a + b
    print(b)
