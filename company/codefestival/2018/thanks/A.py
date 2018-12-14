T, A, B, C, D = map( int, input().split())
ans = 0
if C <= T:
    ans += D
    if A+C <= T:
        ans += B
elif A <= T:
    ans += B
print(ans)
