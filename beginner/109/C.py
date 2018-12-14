def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return(a)

N, K = map( int, input().split())
X = list( map( int, input().split()))
now = abs( K - X[0])
for x in X:
    now = gcd(now, abs(x-K))
print(now)
