import sys
input = sys.stdin.readline
from collections import Counter
def main():
    N = int( input())
    Ss = [ input().strip() for _ in range(N)]
    left = 0
    right = 0
    Up = []
    Down = []
    Sig = []
    for S in Ss:
        C = Counter(S)
        left += C["("]
        right += C[")"]
        now = 0
        p = [0]
        for s in S:
            if s == "(":
                now += 1
            else:
                now -= 1
            p.append(now)
        m = -min(p)
        s = p[0]+m
        g = p[-1]+m
        if s == g:
            Sig.append((s, s, g))
        elif s < g:
            Up.append((s ,s, g))
        else:
            Down.append((s,s,g))
    if left != right:
        print("No")
        return
    Up.sort()
    Down.sort(reverse=True)
    now = 0
    print(Up)
    print(Sig)
    print(Down)
    for m,s,g in Up:
        if now < m:
            print("No")
            return
        now += g-s
    for m,s,g in Sig:
        if now < m:
            print("No")
            return
    for m,s,g in Down:
        if now < m:
            print("No")
            return
        now += g-s
    print("Yes")
if __name__ == '__main__':
    main()
