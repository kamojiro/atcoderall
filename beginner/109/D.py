H, W = map( int, input().split())
A = []
for _ in range(H):
    a = list( map( int, input().split()))
    A.append(a)
N = 0
ANS = []
for i in range(H):
    for j in range(W):
        if A[i][j]%2 == 0:
            pass
        else:
            if j == W-1:
                if i == H-1:
                    pass
                else:
                    A[i][j] -= 1
                    A[i+1][j] += 1
                    N += 1
                    ANS.append([i+1, j+1, i+2, j+1])
            else:
                A[i][j] -= 1
                A[i][j+1] += 1
                ANS.append([i+1,j+1,i+1,j+2])
                N += 1
print(N)
for a in ANS:
    a = map( str, a)
    print(' '.join(a))
