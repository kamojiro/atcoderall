N = int( input())
s = list( input())
I = ['S', 'W']
Flag = False
for x in I:
    for y in I:
        ANS = ['']*N
        ANS[0] = x
        ANS[-1] = y
        for i in range(N-2):
            if ANS[i] == 'S':
                if s[i] == 'o':
                    ANS[i+1] = ANS[i-1]
                else:
                    if ANS[i-1] == 'S':
                        ANS[i+1] = 'W'
                    else:
                        ANS[i+1] = 'S'
            else:
                if s[i] == 'x':
                    ANS[i+1] = ANS[i-1]
                else:
                    if ANS[i-1] == 'S':
                        ANS[i+1] = 'W'
                    else:
                        ANS[i+1] = 'S'
        if ANS[-2] == 'S':
            if s[-2] == 'o':
                if ANS[-3] == ANS[-1]:
                    pass
                else:
                    continue
            else:
                if ANS[-3] == ANS[-1]:
                    continue
                else:
                    pass
        else:
            if s[-2] == 'o':
                if ANS[-3] != ANS[-1]:
                    pass
                else:
                    continue
            else:
                if ANS[-3] != ANS[-1]:
                    continue
                else:
                    pass
        if ANS[-1] == 'S':
            if s[-1] == 'o':
                if ANS[-2] == ANS[0]:
                    pass
                else:
                    continue
            else:
                if ANS[-2] == ANS[0]:
                    continue
                else:
                    pass
        else:
            if s[-1] == 'o':
                if ANS[-2] != ANS[0]:
                    pass
                else:
                    continue
            else:
                if ANS[-2] != ANS[0]:
                    continue
                else:
                    pass
        print(''.join(ANS))
        Flag = True
        break
    if Flag:
        break
if Flag == False:
    print(-1)
