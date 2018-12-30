N = int( input())
X = [ list( map( int, input().split())) for _ in range(N)]
X.sort()
a, b = X[-1]
print(a + b )
