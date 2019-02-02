s = input()
t = input()
ls = len( s)
lt = len( t)
ANS = [ [""]*(ls+1) for _ in range(lt+1) ]
CNT = [ [0]*(ls+1) for _ in range(lt+1)]
for i in range(1,lt+1):
    for j in range(1,ls+1):
        if s[j-1] == t[i-1]:
            ANS[i][j] = ANS[i-1][j-1]+s[j-1]
            CNT[i][j] = CNT[i-1][j-1]+1
        else:
            if CNT[i][j-1] >= CNT[i-1][j]:
                ANS[i][j] = ANS[i][j-1]
                CNT[i][j] = CNT[i][j-1]
            else:
                ANS[i][j] = ANS[i-1][j]
                CNT[i][j] = CNT[i-1][j]
print( ANS[lt][ls])
