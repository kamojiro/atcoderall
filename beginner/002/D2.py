from itertools import combinations
N, M = map( int, input().split())
X = [ tuple( map(int, input().split())) for _ in range(M)]
Flag = False
if M == 0:
    print(1)
    Flag = True
for i in range(N,0,-1):
    Z = list(combinations(range(1,N+1),i))
    for coms in Z:
        K = list(combinations( coms, 2))
        for j in K:
            if j not in X:
                break
        else:
            print(i)
            Flag = True
            break
    if Flag:
        break
                
