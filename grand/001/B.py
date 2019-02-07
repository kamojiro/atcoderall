N, X = map( int, input().split())
a, b = max(X, N-X), min(X, N-X) #a >= b
ans = a + b
if a == b:
    ans += a
while a != b:
    if a%b == 0:
        ans += (a//b*2-1)*b
        break
    ans += a//b*2*b
    a, b = b, a%b
print(ans)
