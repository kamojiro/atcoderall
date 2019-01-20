s = input()
t = input()
ls = len( s)
lt = len( t)
if ls  > lt:
    s, t = t, s
    ls, lt = lt, ls
LCS = [ [0]*(lt+1) for _ in range( ls+1)]
LC = [ [""]*(lt+1) for _ in range(ls+1)]
for i in range(2, lt+1):
    for j in range(1, i): #check (j, i-j)
        if s[j-1] == t[i-j-1]:
            LCS[j][i-j] = LCS[j-1][i-j-1] + 1
        else:
            LCS[j][i-j] = max( LCS[j][i-j-1], LCS[j-1][i-j-1])
for i in range(1,ls -lt+1):
    for j in range(1, lt): #(i, lt - j)
        if s[i-1] == t[lt-j-1]:
            LCS[i][lt-j] = LCS[i-1][lt-j-1] + 1
        else:
            LCS[i][lt-j] = max( LCS[i-1][lt-j], LCS[i][lt-j-1])
for i in range(1, lt+1):
    for j in range(lt - i): #(i+j, ls-j)
        if s[i+j-1] == t[ls-j-1]:
            LCS[i+j][ls-j] = LCS[i+j-1][ls-j-1] + 1
        else:
            LCS[i+j][ls-j] = max( LCS[i+j][ls-j-1], LCS[i+j-1][ls-j])
print( LCS[lt][ls])
