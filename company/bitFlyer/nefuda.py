N = int(input())
A = [int(input()) for i in range(N)]
flag = False
i = 0
for j in range(1,11):
    for k in A:
        if k%(10**j) == 0:
            pass
        else:
            print(i)
            flag = True
            break
    if flag == True:
        break
    i += 1
        
    
