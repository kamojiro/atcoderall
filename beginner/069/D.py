H, W = map( int, input().split())
N = int( input())
A = list( map( int, input().split()))
reverse = 0
ANS = [ [] for _ in range(H)]
gyou = 0
cnt = 0
for i in range(N):
    for j in range(A[i]):
        cnt += 1
        if reverse == 0:
            ANS[gyou].append(i+1)
        else:
            ANS[gyou].insert(0, i+1)
        if cnt == W:
            cnt = 0
            gyou += 1
            reverse = (reverse+1)%2
for i in range(H):
    for j in range(W-1):
        print( str(ANS[i][j]), end = ' ')
    print(ANS[i][W-1])
    
    
