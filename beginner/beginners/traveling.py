N = int(input())
P = [list(map(int, input().split())) for i in range(N)]
Q = [[0,0,0]]
P = Q + P
R = []
S = []
for i in range(N):
    R = R + [[P[i+1][0]-P[i][0], abs(P[i+1][1]-P[i][1]) + abs(P[i+1][2]-P[i][2])]]
for i in range(N):
    if R[i][0] < R[i][1]:
        print("No")
        break
else:
    for i in range(N):
        S = S + [(R[i][0]-R[i][1])%2]
    if sum(S) != 0:
        print("No")
    else:
        print("Yes")
