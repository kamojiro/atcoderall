N = int( input())
X = [ list( map( int, input().split())) for _ in range(N)]
for j in range(N):
    if X[j][2] != 0:
        k = j
        break
A = X[j]
for cx in range(101):
    for cy in range(101):
        H = A[2] + abs( A[0] - cx) + abs( A[1] - cy)
        Flag = True
        for i in range(N):
            if max( H - abs(X[i][0]-cx) - abs(X[i][1] - cy), 0) != X[i][2]:
                Flag = False
                break
        if Flag:
            print('{} {} {}'.format(cx, cy, H))
            break
    if Flag:
        break

            
