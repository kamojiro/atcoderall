#import sys
#input = sys.stdin.readline
from collections import Counter
from copy import deepcopy
def main():
    s = list( input())
    N = len(s)
    C = Counter(s)
    ans = 100
    for i in range(26):
        S = deepcopy(s)
        a = chr( ord("a") + i)
        t = N
        c = C[a]
        if c == 0:
            continue
        # print(a, t, c)
        while t > c:
            t -= 1
            for j in range(t):
                if S[j] != a and S[j+1] == a:
                    S[j] = a
                    c += 1
            if S[t] == a:
                c -= 1
        # print( a, N-t)
        if N-t < ans:
            ans = N-t
    print(ans)
if __name__ == '__main__':
    main()
