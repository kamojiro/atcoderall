N = int(input())
B = [[0]*3]*N
for i in range(N):
    B[i] = list(map(int,input().split()))
ans = 'Yes'
B.insert(0,[0,0,0])
for i in range(N):
    T = B[i+1][0] - B[i][0] 
    S = abs(B[i+1][1] - B[i][1]) + abs(B[i+1][2] - B[i][2])
    if T >= S and (T - S)%2 == 0:
        pass
    else:
        ans = 'No'
        break
print(ans)
