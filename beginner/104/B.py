S = input()
L = len(S)
Flag = True
if not S[0] == 'A':
    Flag = False
cnt = 0
a = str(S[1])
for i in range(2,L-1):
    if S[i] == 'C':
        cnt += 1
    else:
        a += S[i]
a += S[-1]
if a.islower() and cnt == 1:
    pass
else:
    Flag = False
if Flag:
    print('AC')
else:
    print('WA')
    
    
