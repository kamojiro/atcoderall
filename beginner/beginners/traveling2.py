N = int(input())
P = [list(map(int, input().split())) for i in range(N)]
Q = [[0,0,0]]
P = Q + P
for i in range(N):
    if ( P[i+1][0] - P[i][0] ) >= ( abs( P[i+1][1] - P[i][1] ) + abs( P[i+1][2] - P[i][2] )) and ( abs( P[i+1][0] - P[i][0] )-( abs( P[i+1][1] - P[i][1] ) + abs( P[i+1][2] - P[i][2] ))%2 == 0:
        pass
    else:
        print("No")
        break
else:
    print("Yes")
