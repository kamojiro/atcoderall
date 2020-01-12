def main():
    H, W = map( int, input().split())
    S = [ list( input()) for _ in range(H)]
    B = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                B[i][j] = 1
    ANS = [[4000]*(H*W) for i in range(H*W)]
    for i in range(H):
        for j in range(W):
            if B[i][j] == 1:
                continue
            if i > 0:
                if B[i-1][j] == 0:
                    ANS[i*W+j][(i-1)*W+j] = 1
            if i < H-1:
                if B[i+1][j] == 0:
                    ANS[i*W+j][(i+1)*W+j] = 1
            if j > 0:
                if B[i][j-1] == 0:
                    ANS[i*W+j][i*W+j-1] = 1
            if j < W-1:
                if B[i][j+1] == 0:
                    ANS[i*W+j][i*W+j+1] = 1
    for k in 
            

                
    
    print(ans)
            
if __name__ == '__main__':
    main()
