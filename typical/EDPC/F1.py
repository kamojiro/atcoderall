s = input()
t = input()
ls = len( s)
lt = len( t)
if ls  > lt:
    s, t = t, s
    ls, lt = lt, ls
LCS = [ [0]*(ls+1) for _ in range( lt+1)]
LC = [ [""]*(ls+1) for _ in range(lt+1)]
for i in range(2, lt+1):
    for j in range(1, i): #check (j, i-j)
        if s[j-1] == t[i-j-1]:
            LCS[j][i-j] = LCS[j-1][i-j-1] + 1
            LC[j][i-j] = LC[j-1][i-j-1] + s[j-1]
        else:
            if LCS[j][i-j-1] <= LCS[j-1][i-j]:
                LC[j][i-j] = LC[j-1][i-j]
            else:
                LC[j][i-j] = LC[j][i-j-1]
for i in range(1,ls -lt+1):
    for j in range(1, lt): #(i, lt - j)
        if s[i-1] == t[lt-j-1]:
            LCS[i][lt-j] = LCS[i-1][lt-j-1] + 1
            LC[i][lt-j] = LC[i-1][lt-j-1] + s[i-1]
        else:
            if LCS[i-1][lt-j] <= LCS[i][lt-j-1]:
                LC[i][lt-j] = LC[i][lt-j-1]
            else:
                LC[i][lt-j] = LC[i-1][lt-j]
for i in range(1, lt+1):
    for j in range(lt - i): #(i+j, ls-j)
        if s[i+j-1] == t[ls-j-1]:
            LCS[i+j][ls-j] = LCS[i+j-1][ls-j-1] + 1
            LC[i+j][ls-j] = LC[i+j-1][ls-j-1] + s[i+j-1]
        else:
            if LCS[i+j][ls-j-1] <= LCS[i+j-1][ls-j]:
                LC[i+j][ls-j] = LC[i+j-1][ls-j]
            else:
                LC[i+j][ls-j] = LC[i+j][ls-j-1]
print(LC)
print( LC[lt][ls])
