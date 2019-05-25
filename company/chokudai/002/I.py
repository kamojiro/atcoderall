from math import ceil
N = int( input())
A = [0]*N
B = [0]*N
ans = 0
t = 0
for i in range(N):
    A[i], B[i] = map( int, input().split())
nowa = A[0]
nowb = B[0]

for i in range(1,N):
    if ceil(nowa/B[i]) > ceil(A[i]/nowb):
        continue
    elif ceil(nowa/B[i]) == ceil(A[i]/nowb):
        continue
    else:
        nowa, nowb = A[i], B[i]
        t = i
for i in range(N):
    if i == t:
        continue
    if ceil(nowa/B[i]) <= ceil(A[i]/nowb):
        ans = -1
        break
if ans == -1:
    print(ans)
else:
    print(t+1)
