#import sys
#input = sys.stdin.readline
from collections import deque
def main():
    S = input()
    N = len(S)
    ANS = [0]*N
    C = []
    now = "R"
    c = 0
    for i in range(N):
        if now == S[i]:
            c += 1
        else:
            C.append(c)
            now = S[i]
            c = 1
    C.append(c)
    t = len(C)
    NOW = [0]*t
    r = 0
    l = 0

    for i in range(t//2):
        r = (C[i*2]+1)//2 + C[i*2+1]//2
        l = (C[i*2])//2 + (C[i*2+1]+1)//2
        NOW[i*2] = r
        NOW[i*2+1] = l
    d = deque(NOW)
    ANS = [0]*N
    now = "R"
    for i in range(N):
        if now == "R" and S[i] == "L":
            ANS[i-1] = d.popleft()
            ANS[i] = d.popleft()
        now = S[i]
    print( " ".join( map( str, ANS)))
if __name__ == '__main__':
    main()

    
