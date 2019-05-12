N = int( input())
S = [ input() for _ in range(N)]
ans = 0
A = 0
B = 0
T = 0
for s in S:
    t = 0
    if s[0] == "B":
        B += 1
        t += 1
    if s[-1] == "A":
        A += 1
        t += 1
    if t == 2:
        T += 1
    for i in range( len(s)-1):
        if s[i] == "A" and s[i+1] == "B":
            ans += 1
if A == B:
    if A == 0:
        pass
    elif T == A:
        ans += A-1
    else:
        ans += min(A,B)
else:
    ans += min(A,B)
print(ans)
