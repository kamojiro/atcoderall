from bisect import bisect_right,bisect
C, D = map( int, input().split())
m = C//140
M = D//170
ans = 0
L = []
for i in range(1,6):
    L.append(140*i)
    L.append(170*i)
S = [30*i for i in range(1,6)]
if C >= 140*6:
    ans = D - C
elif D >= 170*5:

else:
    k = bisect_right(L,C)
    u = bisect(L,D)
    if k%2 == 0:
        if u%2 == 1:
            for i in range(k/2+1,(u+1)/2):
                ans += 30*i
        else:
            
            
            
    
    
    
    
