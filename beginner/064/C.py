N = int( input())
A = list( map( int, input().split()))
C = [0]*8
col = 0
for a in A:
    for i in range(8):
        if a < (i+1)*400:
            C[i] = 1
            break
    else:
        col += 1
if sum(C) == 0:
    print("{} {}".format( 1, col))
else:
    print("{} {}".format( sum(C), sum(C)+col))


