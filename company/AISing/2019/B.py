N = int( input())
A, B = map( int, input().split())
P = list( map( int, input().split()))
X = Y = Z = 0
for i in range(N):
    if P[i] <= A:
        X += 1
    elif P[i] <= B:
        Y += 1
    else:
        Z += 1
print( min( [X,Y,Z]))
