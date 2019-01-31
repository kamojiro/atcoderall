N, M = map( int, input().split())
ans = "-1 -1 -1"
for i in range(M//3+1):
    if (M-i*3)%2 == 0 and M >= i*3:
        y = (M-i*3)//2 - (N-i)
        x = (N-i) - y
        if x >= 0 and y >= 0:
            ans = str(x) + " " + str(i) + " " + str(y)
            break
print( ans)
