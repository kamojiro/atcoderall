s = input()
t = input()
ls = len( s)
lt = len( t)
LCS = [ [0]*(ls+1) for _ in range( lt+1)]
LC = [ [""]*(ls+1) for _ in range(lt+1)]
for i in range(1,lt+1):
    for j in range(1, ls+1):
        if t[i-1] == s[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
            LC[i][j] = LC[i-1][j-1] + t[i-1]
        else:
            if LCS[i][j-1] <= LCS[i-1][j]:
                LCS[i][j] = LCS[i-1][j]
                LC[i][j] = LC[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]
                LC[i][j] = LC[i][j-1]
print(LC[lt][ls])
