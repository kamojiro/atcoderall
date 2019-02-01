from itertools import accumulate
N, Q = map( int, input().split())
check = [0]*(N+1)
for _ in range(Q):
    l, r = map( int, input().split())
    check[l-1] += 1
    check[r] -= 1
ANS = list( map( lambda x:x%2, accumulate(check)))
ans = ""
for i in range(N):
    if ANS[i] == 0:
        ans += "0"
    else:
        ans += "1"
print( ans)
