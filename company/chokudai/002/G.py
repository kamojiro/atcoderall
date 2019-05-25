def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return(a)
N = int( input())
for _ in range(N):
    a, b = map( int, input().split())
    print( gcd(a,b))
