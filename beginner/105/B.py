N = int(input())
Flag = False
for i in range(26):
    K = N - 4*i
    if K >= 0:
        if K%7 == 0:
            Flag = True
if Flag == True:
    print('Yes')
else:
    print('No')
