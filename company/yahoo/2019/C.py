K, A, B = map( int, input().split())
ans = 0
if A+1 <= K:
    t = (K+1)//(A+2)
    ans = t*B + (K - ((A+2)*t-1))

twoans = A
now = A-1
if A*2 < B:
    while now < K:
        if now + twoans//A*2 <= K:
            now += twoans//A*2
            twoans = twoans - (twoans//A*A) + (twoans//A*B)
        else:
            break
if (K - now)%2 == 0:
    twoans = twoans + (K-now)//2*(B-A)
else:
    twoans = twoans + (K-now)//2*(B-A)+1
print( max(twoans,  ans, K+1))
