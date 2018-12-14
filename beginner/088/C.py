C = [[0]*3]*3
for i in range(3):
    C[i] = list(map(int,input().split()))
ans = 'Yes'
for i in range(3):
    j = (i+1)%3
    if C[i][0] - C[j][0] == C[i][1] - C[j][1] and C[i][1] - C[j][1] == C[i][2] - C[j][2]:
        pass
    else:
        ans = 'No'
for i in range(3):
    j = (i+1)%3
    if C[0][i] - C[0][j] == C[1][i] - C[1][j] and C[1][i] - C[1][j] == C[2][i] - C[2][j]:
        pass
    else:
        ans = 'No'
print(ans)






