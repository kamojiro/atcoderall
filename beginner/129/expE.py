N = 8
cnt = 0
for i in range(N):
    for j in range(N):
        if i+j == i^j and i+j <= 3:
            print(i,j,i+j, i^j)
            cnt += 1
print(cnt)










