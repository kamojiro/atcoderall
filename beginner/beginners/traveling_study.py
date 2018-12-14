N = int(input())
flg = True
cnt,now,posx,posy=0,0,0,0
while cnt < N and flg:
    t,x,y=map(int,input().split())
    if (abs(x-posx)+abs(y-posy)) <= (t-now) and (abs(x-posx)+abs(y-posy)-(t-now))%2 == 0:
        cnt += 1
        now = t
        posx = x
        posy = y
    else:
        print("No")
        flg = False
if flg:
    print("Yes")
