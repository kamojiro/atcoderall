#import sys
#input = sys.stdin.readline
from math import sqrt
def main():
    N = int( input())
    SX = [0 for _ in range(4)]
    SY = [0 for _ in range(4)]
    x_plus = 0
    x_minus = 0
    y_plus = 0
    y_minus = 0
    for _ in range(N):
        x, y = map( int, input().split())
        if x >= 0:
            if y >= 0:
                SX[0] += x
                SY[0] += y
            if y <= 0:
                SX[1] += x
                SY[1] += y
        if x <= 0:
            if y >= 0:
                SX[2] += x
                SY[2] += y
            if y <= 0:
                SX[3] += x
                SY[3] += y

        if x == 0:
            if y > 0:
                y_plus += y
            else:
                y_minus += y
        if y == 0:
            if x > 0:
                x_plus += x
            else:
                x_minus += x
    ans = 0
    print(SX, SY, y_plus)
    for i in range(4):
        if ans**2 < SX[i]**2 + SY[i]**2:
            ans = sqrt(SX[i]**2 + SY[i]**2)
    print(ans)
    S = (SX[0]+SX[3]-x_plus)**2 + (SY[0]+SY[3])**2
    if ans**2 < S:
        ans = sqrt(S)
    S = (SX[1]+SX[2]-x_minus)**2 + (SY[1]+SY[2])**2
    if ans**2 < S:
        ans = sqrt(S)
    S = (SX[0]+SX[1])**2 + (SY[0]+SY[1] - y_plus)**2
    if ans**2 < S:
        ans = sqrt(S)
    S = (SX[2]+SX[3])**2 + (SY[2]+SY[3] - y_minus)**2
    if ans**2 < S:
        ans = sqrt(S)
    
    print(ans)
        
if __name__ == '__main__':
    main()
