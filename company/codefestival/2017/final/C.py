N = int( input())
D = list( map( int, input().split()))
D.sort()
ans = 24
c = 1
A = []
B = []
now = 0
for i in range(N):
    if D[i] == now:
        c += 1
    if c == 2:
        ans = 0
    if i%2 == 0:
        A.append(D[i])
    else:
        B.append(D[i])
s = 0
if A:
    for a in A:
        ans = min(ans, a-s)
        s = a
s = 0
if B:
    for b in B:
        ans = min(ans, b-s)
        s=b
if A and B:
    ans = min( ans, 24-A[-1]-B[-1], A[-1]+B[-1])
print(ans)
