N = int( input())
B = list( map( int, input().split()))
C = [0]*(N+1)
ans = 0
for i in range(N):
    if B[i] > i+1:
        ans = -1
        break
ANS = []
if ans == 0:
    for i in range(1, N+1):
        L = []
        for j in range(N):
            if 1 <= B[j] <= i:
                L.append(B[j])
        now = i-1
        for s in L[::-1]:
            if s == i:
                ANS.insert(now,i)
            now += 1
if ans == -1:
    print(-1)
else:
    for i in range(N):
        print(ANS[i])
