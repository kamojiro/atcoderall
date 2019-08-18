#import sys
#input = sys.stdin.readline
from collections import Counter
from itertools import accumulate
def main():
    s = input()
    t = input()
    S = Counter(s)
    T = Counter(t)
    N = len(t)
    M = len(s)
    d = dict()
    for i in range(26):
        d[ chr( ord("a") + i)] = i
    for key in T:
        if S[key] == 0:
            print(-1)
            return
    Al = [[0]*M for _ in range(26)]
    a = ord("a")
    for i in range(M):
        Al[d[s[i]]][i] = 1
    Ac = [[0]*M for _ in range(26)]
    for i in range(26):
        now = -1
        for j in range(M-1,-1,-1):
            Ac[i][j] = now
            if Al[i][j] == 1:
                now = j
    ans = 1
    for i in range(M):
        if t[0] == s[i]:
            now = i
            break
    first = d[s[0]]
    for cnt in range(1,N):
        g = d[t[cnt]]
        if Ac[g][now] == -1:
            ans += 1
            if g == first:
                now = 0
            else:
                now = Ac[g][0]
        else:
            now = Ac[g][now]
    print(M*(ans-1)+now+1)
    
if __name__ == '__main__':
    main()
