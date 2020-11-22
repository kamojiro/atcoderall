import sys
input = sys.stdin.readline
def main():

    H, W, N, M = map(int, input().split())
    MAP = [[0] * W for _ in range(H)]
    ANS = [[0] * W for _ in range(H)]
    
    for _ in range(N):
        A, B = map(int, input().split())
        MAP[A-1][B-1] = 1
    for _ in range(M):
        C, D = map(int, input().split())
        MAP[C-1][D-1] = -1
    
    for i in range(H):
        light = False
        for j in range(W):
            if MAP[i][j] == 1:
                light = True
            elif MAP[i][j] == -1:
                light = False
    
            if light:
                ANS[i][j] = 1
    
        light = False
        for j in range(W-1, -1, -1):
            if MAP[i][j] == 1:
                light = True
            elif MAP[i][j] == -1:
                light = False
            
            if light:
                ANS[i][j] = 1
    
    for j in range(W):
        light = False
        for i in range(H):
            if MAP[i][j] == 1:
                light = True
            elif MAP[i][j] == -1:
                light = False
    
            if light:
                ANS[i][j] = 1
    
        light = False
        for i in range(H-1, -1, -1):
            if MAP[i][j] == 1:
                light = True
            elif MAP[i][j] == -1:
                light = False
            if light:
                ANS[i][j] = 1
    
    ans = 0
    for a in ANS:
        ans += sum(a)
    
    print(ans)

if __name__ == '__main__':
    main()

