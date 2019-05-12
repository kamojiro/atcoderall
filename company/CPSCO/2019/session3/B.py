N, M = map( int, input().split())
A = list( map(int, input().split()))
A.sort(reverse=True)
ans = 0
for a in A:
    ans += 1
    if M <= a:
        break
    else:
        M -= a
print(ans)
