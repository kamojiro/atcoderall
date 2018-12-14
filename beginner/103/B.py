S = input()
T = input()
ans = 'No'
M = len(S)
if len(S) != len(T):
    pass
else:
    for i in range(M):
        SK = ''
        for j in range(M):
            SK += S[(j+i)%M]
        if T == SK:
            ans = 'Yes'
            break
print(ans)







