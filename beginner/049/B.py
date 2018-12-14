H, W = map( int, input().split())
C = [ input() for _ in range(H)]
ANS = [""]*(H*2)
for i in range(H*2):
    print(C[i//2])
        
