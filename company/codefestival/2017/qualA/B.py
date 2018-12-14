N, M, K = map( int, input().split())
Flag = False
ans = 'No'
for i in range(N+1):
    for j in range(M+1):
        if (M-j)*i + (N-i)*j == K:
            ans = 'Yes'
            Flag = True
            break
    if Flag == True:
        break
print(ans)
