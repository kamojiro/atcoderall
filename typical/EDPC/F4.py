s = input()
t = input()
ls = len( s)
lt = len( t)
CNT = [ [0]*(ls+1) for _ in range(lt+1)]
for i in range(1,lt+1):
    for j in range(1,ls+1):
        if s[j-1] == t[i-1]:
            CNT[i][j] = CNT[i-1][j-1]+1
        else:
            if CNT[i][j-1] >= CNT[i-1][j]:
                CNT[i][j] = CNT[i][j-1]
            else:
                CNT[i][j] = CNT[i-1][j]
i = lt
j = ls
ans = ""
while i > 0 and j > 0:
    if t[i-1] == s[j-1]:
        ans += t[i-1]
        i -= 1
        j -= 1
    else:
        if CNT[i-1][j] > CNT[i][j-1]:
            i -= 1
        else:
            j -= 1
print( ans[::-1])
