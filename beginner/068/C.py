N, M = map( int, input().split())
fromN = set([])
from1 = set([])
ans = 'IMPOSSIBLE'
for _ in range(M):
    a, b = map( int, input().split())
    a, b = a-1, b-1
    if a == 0:
        if b == N-1:
            ans = 'POSSIBLE'
            break
        else:
            from1.add(b)
    elif b == N-1:
        fromN.add(a)
if len( fromN & from1) != 0:
    ans = 'POSSIBLE'
print(ans)
            
        
    







