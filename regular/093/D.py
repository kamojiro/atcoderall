Q = int( input())
for _ in range(Q):
    A, B = map( int, input().split())
    print( min(A, B)*2 - 1)
