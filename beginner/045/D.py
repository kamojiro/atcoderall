from collections import defaultdict
H, W, N = map( int, input().split())
D = defaultdict( int)
def check(t):
    a, b = t
    if a == 0 or a == H-1:
        return False
    if b == 0 or b == W-1:
        return False
    return True
for _ in range(N):
    a, b = map( int, input().split())
    a, b = a-1, b-1
    if a >= 1:
        if b >= 1:
            D[(a-1,b-1)] += 1
        if b < W-1:
            D[(a-1,b+1)] += 1
        D[(a-1,b)] += 1
    if a < H-1:
        if b >= 1:
            D[(a+1,b-1)] += 1
        if b < W-1:
            D[(a+1,b+1)] += 1
        D[(a+1,b)] += 1
    if b >= 1:
        D[(a,b-1)] += 1
    if b < W-1:
        D[(a,b+1)] += 1
    D[(a,b)] += 1
ANS = [0]*10
for c in D:
    if check(c):
        ANS[D[c]] += 1
ANS[0] = (H-2)*(W-2)- sum(ANS)
for ans in ANS:
    print(ans)
