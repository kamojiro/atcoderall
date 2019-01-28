a, b = map( int, input().split())
C = [0,1,2,3,2,1,2,3,3,2,1]
c = abs( a-b)

print( c//10 + C[c-c//10*10])
