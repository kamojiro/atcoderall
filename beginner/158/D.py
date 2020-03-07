import sys
input = sys.stdin.readline
from collections import deque
def main():
    S = input().strip()
    Q = int( input())
    Query = [ input().strip() for _ in range(Q)]
    now = 0
    ANS = deque(['1'])
    t = 0
    for q in Query:
        if q == '1':
            if now == 0:
                now = 1
            else:
                now = 0
            continue
        t += 1
        _, f, c = q.split()
        if f == '1':
            if now == 0:
                ANS.appendleft(c)
            else:
                ANS.append(c)
        else:
            if now == 0:
                ANS.append(c)
            else:
                ANS.appendleft(c)
    for i in range(t+1):
        if ANS[i] == '1':
            if now == 0:
                ANS[i] = S
            else:
                ANS[i] = S[::-1]
    if now == 1:
        ANS.reverse()
    print("".join(ANS))
    
if __name__ == '__main__':
    main()
