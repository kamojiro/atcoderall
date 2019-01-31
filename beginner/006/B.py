a = 0
b = 0
c = 1
n = int( input())
for _ in range(3,n):
    d = a + b + c
    d %= 10007
    a, b, c = b, c, d
if n == 1:
    print(a)
elif n == 2:
    print(b)
elif n == 3:
    print(c)
else:
    print( d)
