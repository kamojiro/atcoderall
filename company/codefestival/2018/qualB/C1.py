N = int( input())
ANS = ['']*N
ans = ''
for j in range(N):
    if j == N-1:
        ans += 'X'
    elif (j+2)%4 == 0:
        ans += 'X'
    else:
        ans += '.'
ANS[0] = ans

for i in range(1,N):
    ans = ''
    if i%4 == 0:
        k = 2
    elif i%4 == 1:
        k = 0
    elif i%4 == 2:
        k = 1
    else:
        k = 3
    for j in range(N-1):
        if (j+k)%4 == 0:
            ans += 'X'
        else:
            ans += '.'
    if k == 0:
        ans += 'X'
    elif k == 3:
        ans += 'X'
    else:
        ans += '.'
    ANS[i] = ans
     
ANS[N-1] = 'X'*N
from collections import Counter
s = 0

for i in range(N):
    print(ANS[i])
    s += Counter(ANS[i])['X']
print(s)










