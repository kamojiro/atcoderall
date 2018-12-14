N, Y  = map( int, input().split())
Y = Y/1000
ichiman = -1
gosen = -1
sen = -1
Flag = False
if N*10 < Y:
    Flag = True
for i in range(N+1):
    for j in range(N-i+1):
        if i*10 + j*5 + (N-i-j) == Y:
            ichiman = i
            gosen = j
            sen = N-i-j
            Flag = True
            break
    if Flag:
        break

print('{} ' '{} ' '{}'.format(ichiman, gosen, sen))
