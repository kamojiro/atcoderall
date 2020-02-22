import sys
input = sys.stdin.readline
from collections import defaultdict
def main():
    N = int( input())
    S = [ input().strip() for _ in range(N)]
    d = defaultdict( int)
    for s in S:
        d[s] += 1
    m = 0
    for _, v in d.items():
        if v > m:
            m = v
    ANS = []
    for w, v in d.items():
        if v == m:
            ANS.append(w)
    ANS.sort()
    print("\n".join(ANS))
if __name__ == '__main__':
    main()
