M, K = map( int, input().split())
ANS = []
ans = 0
if M == 0:
    if  K == 0:
        ans = 0
        ANS = [0,0]
    else:
        ans = -1
elif M == 1:
    if  K == 0:
        ans = 0
        ANS = [0,0,1,1]
    else:
        ans = -1
elif M >= 2:
    if K >= 2**M:
        ans = -1
if M >= 2 and ans == 0:
    ANS = list( range(K+1)) + list( range(K))[::-1] + list( range(K,2**M))[::-1] + list(range(K+1,2**M))
if ans == -1:
    print(ans)
else:
    print(" ".join( map( str, ANS)))
