a, b = map( int, input().split())
a %= 2
b %= 4
ans = "Devil"
if a == 0:
    if b == 1 or b == 2:
        ans = "Angel"
else:
    if b != 0:
        ans = "Angel"
print(ans)

