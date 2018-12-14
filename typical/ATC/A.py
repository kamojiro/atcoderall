from collections import Counter
H, W = map( int, input().split())
roads = [ list(input()) for _ in range(H)]
for i in range(H):
    if 's' in roads[i]:
        sx = i
        sy = roads[i].index('s')
        break
Flag = False

def gogo(roads, x, y, Flag):
    if Flag:
        return roads, x, y, Flag
    print('{} {}'.format(x,y))
    roads[x][y] = '#'
    if roads[max(x-1,0)][y] != '#' and Flag == False:
        if roads[x-1][y] == 'g':
            Flag = True
        else:
            x = x - 1
            roads, x1, y1, Flag = gogo(roads, x, y, Flag)
            if Flag == False:
                x
    if roads[min(x+1,H-1)][y] != '#' and Flag == False:
        if roads[x+1][y] == 'g':
            Flag = True
        else:
            x = x + 1
            roads, x, y, Flag = gogo(roads, x, y, Flag)
    if roads[x][max(y-1,0)] != '#' and Flag == False:
        if roads[x][y-1] == 'g':
            Flag = True
        else:
            y = y - 1
            roads, x, y, Flag = gogo(roads, x, y, Flag)
    if roads[x][min(y+1,W-1)] != '#' and Flag == False:
        if roads[x][y+1] == 'g':
            Flag = True
        else:
            y = y + 1
            roads, x, y, Flag = gogo(roads, x, y, Flag)
    
    return roads, x, y, Flag

roads, x, y, Flag = gogo(roads, sx, sy, Flag)
if Flag:
    print('Yes')
else:
    print('No')
