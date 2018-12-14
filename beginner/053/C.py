x = int( input())
a = x//11*2
b = x%11
if b == 0:
    print(a)
elif b <= 6:
    print(1 + a )
else:
    print(2 + a)
