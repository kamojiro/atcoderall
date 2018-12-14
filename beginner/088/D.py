from collections import Counter, deque
H, W = map( int, input().split())
S = [list(input()) for x in range(H)]
white = 0
for i in range(H): #すべての白マスの個数
    white += Counter(S[i])['.']
Goal = False
Able = True
path = 1
Sunuke = [[0,0]]
#通った白マスを黒マスに入れ替える
S[0][0] = '#'
while Goal == False and len(Sunuke) != 0:
    Sunuke_temp = Sunuke
    Sunuke = []
    path += 1
    for x in Sunuke_temp:
        i = x[0]
        j = x[1]
        if (min(i+1,H-1) == H-1 and j == W-1) or (min(j+1,W-1) == W-1 and i == H-1):
            Goal = True
            Sunuke.append([1,1])
            break
        if S[max(i-1,0)][j] == '.':
            #左端の場合は現在地を参照する
            #現在地は黒なのでFalse
            Sunuke.append([i-1,j])
            S[i-1][j] = '#'
        if S[min(i+1,H-1)][j] == '.':
            Sunuke.append([i+1,j])
            S[i+1][j] = '#'
        if S[i][max(j-1,0)] == '.':
            Sunuke.append([i,j-1])
            S[i][j-1] = '#'
        if S[i][min(j+1,W-1)] == '.':
            Sunuke.append([i,j+1])
            S[i][j+1] = '#'
print(-1 if len(Sunuke) == 0 else white - path)
#最後に白マスを数えても良かった
