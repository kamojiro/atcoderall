N = int( input())
ANS = ['']*N
if N%5 == 0:
    l = 1
elif N%5 == 1:
    l = 3
elif N%5 == 2:
    l = 0
elif N%5 == 3:
    l = 2
else:
    l = 4
ans = '.'
if N == 1:
    ANS[0] = 'X'
else:
    for j in range(1,N-1):
        if j%5 == 2 or j%5 == 4:
            ans += 'X'
        else:
            ans += '.'
    ans += 'X'
    ANS[0] = ans
    

for i in range(1,N-1):
    ans = ''
    if i%5 == 4 or i%5 == 1:
        ans = 'X'
    else:
        ans = '.'
    if i%5 == 0:
        k = 3
    elif i%5 == 1:
        k = 0
    elif i%5 == 2:
        k = 2
    elif i%5 == 3:
        k = 4
    else:
        k = 1
    for j in range(1,N-1):
        if (j+k)%5 == 0:
            ans += 'X'
        else:
            ans += '.'
    if i%5 == l or (N-1+k)%5 == 0:
        ans += 'X'
    else:
        ans += '.'
    ANS[i] = ans
ans = ''

#from collections import Counter
s = 0
if N%5 == 0:
    t = 4
elif N%5 == 1:
    t = 2
elif N%5 == 2:
    t = 0
elif N%5 == 3:
    t = 3
else:
    t = 1
for j in range(N-1):
    if j%5 == t or j%5 == (t+2)%5:
        ans += 'X'
    else:
        ans += '.'
ans += 'X'
ANS[N-1] = ans
for i in range(N):
    print(ANS[i])
#    s += Counter(ANS[i])['X']
#print(s)

