from collections import defaultdict
N = int( input())
ad = defaultdict( int)
bd = defaultdict( int)
ansd = defaultdict( int)
A = [0]*N
B = [0]*N
for i in range(N):
    a, b = map( int, input().split())
    A[i], B[i] = a, b
    ad[a] += 1
    bd[b] += 1
ans = 0
for i in range(N):
    a, b = A[i], B[i]
    if ansd[a] == 0:
        ans += 1
        if ansd[b] == 0:
            if ad[a] <= bd[b]:
                ansd[a] += 1
            else:
                ansd[b] += 1
        else:
            ansd[a] += 1
    else:
        if ansd[b] == 0:
            ans += 1
            ansd[b] += 1
    ad[a] -= 1
    bd[b] -= 1
print(ans)










