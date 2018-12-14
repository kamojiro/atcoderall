from collections import deque
H, W = map( int, input().split())
roads = [ list(input()) for _ in range(H)]
for i in range(H):
    if 's' in roads[i]:
        sx = i
        sy = roads[i].index('s')
        break
S = deque([[sx,sy]])
roads[sx][sy] = '#'
Flag = False
while len(S) != 0:
    L = S.pop()
    x, y = L[0], L[1]
    if roads[max(x-1,0)][y] != '#':
        if roads[x-1][y] == 'g':
            Flag = True
            break
        else:
            roads[x-1][y] = '#'
            S.append([x-1,y])
    if roads[min(x+1,H-1)][y] != '#':
        if roads[x+1][y] == 'g':
            Flag = True
            break
        else:
            roads[x+1][y] = '#'
            S.append([x+1,y])
    if roads[x][max(y-1,0)] != '#':
        if roads[x][y-1] == 'g':
            Flag = True
            break
        else:
            roads[x][y-1] = '#'
            S.append([x,y-1])
    if roads[x][min(y+1,W-1)] != '#':
        if roads[x][y+1] == 'g':
            Flag = True
            break
        else:
            roads[x][y+1] = '#'
            S.append([x,y+1])
if Flag:
    print('Yes')
else:
    print('No')
