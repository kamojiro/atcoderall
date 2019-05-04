N, A, B = map( int, input().split())
if B != 0:
    D = list( map( int, input().split()))
    D.sort()
    now = 0
    ans = 0
    D.append(N+1)
    for d in D:
        ans += d - now - 1 - (d-now-1)//A
        now = d
else:
    ans = 0
print(ans)
