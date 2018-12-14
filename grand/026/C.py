N = int(input())
S = input()
S_left = S[:N]
S_right = S[N*2-1:N-1:-1]
for i in range(2**N):
    blue_left = []
    blue_right = []
    red_left = []
    red_right = []
    X = bin(i)[2:]
    for j in X:
        #0=blue,1=red
        if j == 0:
            blue_left = 
            
