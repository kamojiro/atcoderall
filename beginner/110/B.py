N, M, X, Y = map( int, input().split())
x = max( list( map( int, input().split())))
y = min( list( map( int, input().split())))
if max(x, X)+1 <= min( y, Y):
    print('No War')
else:
    print('War')

