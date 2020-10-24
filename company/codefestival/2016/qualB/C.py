import sys
input = sys.stdin.readline
def main():
    W, H = map(int,input().split())
    F = [(int(input()),0,i) for i in range(W)]
    F.extend([(int(input()),1,i) for i in range(H)])
    F.sort(key=lambda x:x[0])
    h, w = H+1, W+1
    ans = 0
    for x, t, i in F:
        if t == 0:
            ans += x*h
            w -= 1
        else:
            ans += x*w
            h -= 1
    print(ans)

if __name__ == '__main__':
    main()
