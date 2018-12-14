N = int( input())
bridge, blue = map( int, input().split())
for _ in range(N-1):
    t, a = map( int, input().split())
    k = max((bridge+t-1)//t, (blue+a-1)//a)
    bridge, blue = k*t, k*a
print( bridge + blue)
