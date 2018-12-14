C, D = map( int, input().split())
a = 140
b = 170
ans = 0
while D > a:
    ans += max(0, min(D,b) - max(C,a))
    a *= 2
    b *= 2
print(ans)
