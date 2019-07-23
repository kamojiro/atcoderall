a, b, c = map( int, input().split())
Q = 10**9 + 7
print(a*b%Q*c%Q)
