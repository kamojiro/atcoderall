from itertools import product
from copy import deepcopy
def depth_search(A,a,b):
    cnt = 0
    S = [[a,b]]
    B = deepcopy(A)
    while len(S) != 0:
        p = S.pop()
        cnt += 1
        x ,y = p[0], p[1]
        if B[max(x-1,0)][y] == 'o':
            S.append([x-1,y])
            B[x-1][y] = 'x'
        if B[min(x+1,9)][y] == 'o':
            S.append([x+1,y])
            B[x+1][y] = 'x'
        if B[x][max(y-1,0)] == 'o':
            S.append([x,y-1])
            B[x][y-1] = 'x'
        if B[x][min(y+1,9)] == 'o':
            S.append([x,y+1])
            B[x][y+1] = 'x'
    return cnt
    
A = [ list(input()) for i in range(10)]
area = 0
for i in range(10):
    for j in range(10):
        if A[i][j] == 'o':
            area += 1
if area >= 93:
    Flag = True
else:
    Flag = False
    for q in product(range(10), repeat = 2):
        a,b = q[0], q[1]
        if A[a][b] == 'x':
            if depth_search(A,a,b) == area+1:
                Flag = True
                break
print('YES' if Flag else 'NO')
        
