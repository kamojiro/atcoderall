#import sys
#input = sys.stdin.readline
from collections import deque
def main():
    N, M = map( int, input().split())
    X = list( map( int, input().split()))
    Y = [deque() for _ in range(M)]
    modM = [0]*M
    for i in range(N):
        Y[X[i]%M].append(X[i])
        modM[X[i]%M] += 1
    ans = 0
    ans += modM[0]//2
    for i in range(1,(M+1)//2):
        x, y = i, M-i
        if modM[x] > modM[y]:
            x, y = y, x
        mx, my = modM[x], modM[y]
        ans += mx
        before = -1
        for z in Y[y]:
            if mx+2 > my:
                break
            if before == z:
                ans += 1
                my -= 2
                before = -1
            else:
                before = z
    if M%2 == 0:
        ans += modM[M//2]//2
    print(ans)
if __name__ == '__main__':
    main()
