H,W = map(int, input().split())
A = [list(input()) for i in range(H)]
Flag = True
for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            if A[max(0, i-1)][j] == '#' or A[min(H-1,i+1)][j] == '#' or A[i][max(0,j-1)] == '#' or A[i][min(W-1,j+1)] == '#':
                pass
            else:
                Flag = False
                break
    if Flag == False:
        break
if H == 1 and W == 1 and A[0][0] == '#':
    Flag = False
if Flag == True:
    print('Yes')
else:
    print('No')
        
        
        

