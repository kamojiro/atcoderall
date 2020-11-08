import sys
input = sys.stdin.readline
def main():
    H, W, N, M = map(int,input().split())
    AB = [ tuple(map(int,input().split())) for _ in range(N)]
    CD = [ tuple(map(int,input().split())) for _ in range(M)]
    board = [[0]*W for _ in range(H)]
    ANS = [[0]*W for _ in range(H)]
    for a, b in AB:
        board[a-1][b-1] = 10
    for c, d in CD:
        board[c-1][d-1] = 100
    for i in range(H):
        light = False
        for j in range(W):
            if board[i][j] == 10:
                light = True
            elif board[i][j] == 100:
                light = False
            if light:
                ANS[i][j] = 1
        light = False
        for j in range(W-1,-1,-1):
            if board[i][j] == 10:
                light = True
            elif board[i][j] == 100:
                light = False
            if light:
                ANS[i][j] = 1

    for j in range(W):
        light = False
        for i in range(H):
            if board[i][j] == 10:
                light = True
            elif board[i][j] == 100:
                light = False
            if light:
                ANS[i][j] = 1
        light = False
        for i in range(H-1,-1,-1):
            if board[i][j] == 10:
                light = True
            elif board[i][j] == 100:
                light = False
            if light:
                ANS[i][j] = 1

    ans = 0
    # print(ANS)
    for p in ANS:
        ans += sum(p)
    print(ans)
if __name__ == '__main__':
    main()
