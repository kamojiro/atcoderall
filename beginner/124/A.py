A, B = map( int, input().split())
print( max([A+ A-1, B + A, B + B -1]))
