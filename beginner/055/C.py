N, M = map( int, input().split())
if N*2 <= M:
    print(N+(M-N*2)//4)
else:
    print(M//2)
