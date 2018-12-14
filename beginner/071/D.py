N = int( input())
SU = list( input())
SD = list( input())
Q = 10**9 + 7
i = 0
yokocnt = 0
tatecnt = 0
ans = 3
while i <= N-1:
    if SU[i] == SD[i]:
        yokocnt = 0
        i += 1
        tatecnt += 1
        if tatecnt >= 2:
            ans = (ans*2)%Q
    else:
        tatecnt = 0
        i += 2
        yokocnt += 1
        if yokocnt >= 2:
            ans = (ans*3)%Q
        else:
            ans = (ans*2)%Q
print(ans)
    
    
