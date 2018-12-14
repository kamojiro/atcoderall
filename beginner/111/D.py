def solution(x,y):
    ans = ''
    nowx, nowy = 0,0
    preX = [0]*31
    preY = [0]*31
    for i in range(31):
        if nowx < x:
            nowx += 2**(30-i)
            preX[i] = 1
        else:
            nowx -= 2**(30-i)
            preX[i] = -1
        if nowy < y:
            nowy += 2**(30-i)
            preY[i] = 1
        else:
            nowy -= 2**(30-i)
            preY[i] = -1
    for i in range(31):
        if preX[i] == -1 and preY[i] == -1:
            ans += 'L'
        elif preX[i] == 1 and preY[i] == 1:
            ans += 'R'
        elif preX[i] == -1 and preY[i] == 1:
            ans += 'D'
        else:
            ans += 'U'
    return ans
N = int( input())
X = [0]*N
Y = [0]*N
x, y = map( int, input().split())
X[0] = x
Y[0] = y
evod = (x+y)%2
Flag = True
for i in range(1,N):
    x, y = map( int, input().split())
    X[i] = x
    Y[i] = y
    if (x+y)%2 != evod:
        Flag = False

if Flag:
    D = [2**i for i in range(30,-1,-1)]
    if evod == 1:
        print(31)
        print(' '.join(map(str,D)))
        for i in range(N):
            print( solution(X[i]+Y[i],X[i]-Y[i]))
    else:
        print(32)
        D.append(1)
        print(' '.join(map(str,D)))
        for i in range(N):
            print( solution(X[i]+Y[i]-1,X[i]-1-Y[i]) + 'R')
else:
    print(-1)
