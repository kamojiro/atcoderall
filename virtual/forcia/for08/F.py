#import sys
#input = sys.stdin.readline
from collections import defaultdict
def main():
    N = int( input())
    XY = [tuple( map( int, input())) for _ in range(N)]
    # d = defaultdict(lambda : False)
    # for xy in XY:
    #     d[xy] = True
    tx = [[] for _ in range(10**5+1)]
    cx = [0]*(10**5+1)
    ty = [[] for _ in range(10**5+1)]
    cy = [0]*(10**5+1)
    for x, y in XY:
        tx[x].append(y)
        cx[x] += 1
        ty[y].append(x)
        cy[y] += 1
    ans = 0
    for x, y in XY:
        fx, fy = x,y
        while (cx[fx] >= 2 and cy[fy] == 1) or (cx[fx] == 1 and cy[fy] >= 2):
            if cy[fy] == 1:
                cy[fy] = 1
                
        
if __name__ == '__main__':
    main()
