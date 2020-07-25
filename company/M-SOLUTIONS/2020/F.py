#import sys
#input = sys.stdin.readline
def get_collision(A,ans):
    A.sort()
    nowkey = -10**10
    prevcoor = -10**10
    ret = ans[0]
    for key, coor, a in A:
        if key != nowkey:
            if a == 1:
                nowkey = key
                prevcoor = coor
                continue
            else:
                continue
        if a == 1:
            prevcoor = coor
            continue
        if (coor - prevcoor)*5 < ret:
            ret = (coor - prevcoor)*5
    ans[0] = ret

def main():
    N = int( input())
    XYU = [ tuple( input().split()) for _ in range(N)]
    U = []
    R = []
    D = []
    L = []
    for x, y, u in XYU:
        x, y = int(x), int(y)
        if u == "U":
            U.append((x,y))
        elif u == "D":
            D.append((x,y))
        elif u == "L":
            L.append((x,y))
        else:
            R.append((x,y))
    ans = [10**10]

    UD = [(x,y,1) for x, y in U] + [(x,y,-1) for x, y in D]
    get_collision(UD, ans)
    LR = [(y,x,1) for x, y in R] + [(y,x,-1) for x, y in L]
    get_collision(LR, ans)
    RU = [(x+y,x-y,1) for x, y in R] + [(x+y,x-y,-1) for x,y in U]
    get_collision(RU, ans)
    LD = [(x+y,x-y,1) for x, y in D] + [(x+y,x-y,-1) for x,y in L]
    get_collision(LD,ans)
    LU = [(x-y,x+y,1) for x,y in U] + [(x-y,x+y,-1) for x,y in L]
    get_collision(LU,ans)
    RD = [(x-y,x+y,1) for x,y in R] + [(x-y,x+y,-1) for x,y in D]
    get_collision(RD,ans)
    if ans[0] < 10**10:
        print(ans[0])
    else:
        print("SAFE")
        
if __name__ == '__main__':
    main()
